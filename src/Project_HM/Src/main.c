/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2019 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define CHUNK_SIZE 512
#define CHUNK_NUM (65536 / CHUNK_SIZE)

uint8_t send_en = 1;

void MX_ADC_Init2(void);
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
ADC_HandleTypeDef hadc;

UART_HandleTypeDef huart2;

/* USER CODE BEGIN PV */
ADC_HandleTypeDef hadc2;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_ADC_Init(void);
static void MX_USART2_UART_Init(void);
/* USER CODE BEGIN PFP */
void User_Init(void);

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
#ifdef __GNUC__
#define PUTCHAR_PROTOTYPE int __io_putchar(int ch)
#define GETCHAR_PROTOTYPE int __io_getchar(void)
#else
#define PUTCHAR_PROTOTYPE int fputc(int ch, FILE *f)
#define GETCHAR_PROTOTYPE int fgetc(FILE *f)
#endif


/* USER CODE BEGIN 0 */
PUTCHAR_PROTOTYPE
{
	HAL_UART_Transmit(&huart2, (uint8_t *)&ch, 1, 0xFFFF);
	return ch;
}

GETCHAR_PROTOTYPE
{
	char ch;
	HAL_UART_Receive(&huart2, (uint8_t *)&ch, 1, 0xFFFF);

	return ch;
}
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  // Vector to store the values of the ADC
  // The first value is the vrefint readout
  // The second is the temperature readout
  /* USER CODE END 1 */
  

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_ADC_Init();

  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */
  __HAL_ADC_ENABLE(&hadc);
  HAL_ADC_Start(&hadc);

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
      uint8_t *base_p = (uint8_t *)0x20000000;
      uint8_t *uid_p = (uint8_t *)0x1FF800D0;

      uint16_t *vdd_cal = (uint16_t *)0x1FF800F8;

      uint16_t *temp30_cal = (uint16_t *)0x1FF800FA;
      uint16_t *temp110_cal = (uint16_t *)0x1FF800FE;

      if(send_en) {
	  // Waffer number
	  printf("%#02x", (uint8_t)*uid_p); uid_p++;

	  // Lot number
	  for(int i = 0; i < 7; ++i)
	      printf("%01X",(uint8_t)*(uid_p + i));

	 // Offset the memory
	 uid_p = (uint32_t *)0x1FF800e4;

	 for(int i = 0; i < 4; ++i) {
	     printf("%01X", (uint8_t)*(uid_p + i)); // X/Y Coords in BCD
	 }
	 printf("\n");

	 // Calibration data for later computations
	 printf("%d\n", *temp30_cal);
	 printf("%d\n", *temp110_cal);
	 printf("%d\n", *vdd_cal);



	 int vdd = HAL_ADC_GetValue(&hadc);
	 HAL_ADC_Stop(&hadc);
	 __HAL_ADC_DISABLE(&hadc);

	 MX_ADC_Init2();
	 __HAL_ADC_ENABLE(&hadc2);
	 HAL_ADC_Start(&hadc2);
	 while(HAL_ADC_PollForConversion(&hadc2, 10) != HAL_OK) {};
	 int temp = HAL_ADC_GetValue(&hadc2);

      	 for(int e = 0; e < CHUNK_NUM; ++e) {
      	     // Memory address of the chunk
      	     printf("%p\n", (void *)base_p);

      	     // Voltage value
      	     printf("%d\n", vdd);

      	     // Temperature value
      	     printf("%d\n", temp);

      	     // Memory dump of the corresponding region
      	     for(int c = 0; c < CHUNK_SIZE; ++c)
      		 printf("%u ", *(base_p + c));
      	     printf("\n");

      	     base_p += CHUNK_SIZE;
      	  }
      	  send_en = 0;
     }
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage 
  */
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  /** Initializes the CPU, AHB and APB busses clocks 
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL3;
  RCC_OscInitStruct.PLL.PLLDIV = RCC_PLL_DIV2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB busses clocks 
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief ADC Initialization Function
  * @param None
  * @retval None
  */
static void MX_ADC_Init(void)
{

  /* USER CODE BEGIN ADC_Init 0 */

  /* USER CODE END ADC_Init 0 */

  ADC_ChannelConfTypeDef sConfig = {0};

  /* USER CODE BEGIN ADC_Init 1 */

  /* USER CODE END ADC_Init 1 */
  /** Configure the global features of the ADC (Clock, Resolution, Data Alignment and number of conversion) 
  */
  hadc.Instance = ADC1;
  hadc.Init.ClockPrescaler = ADC_CLOCK_ASYNC_DIV1;
  hadc.Init.Resolution = ADC_RESOLUTION_12B;
  hadc.Init.DataAlign = ADC_DATAALIGN_RIGHT;
  hadc.Init.ScanConvMode = ADC_SCAN_DISABLE;
  hadc.Init.EOCSelection = ADC_EOC_SINGLE_CONV;
  hadc.Init.LowPowerAutoWait = ADC_AUTOWAIT_DISABLE;
  hadc.Init.LowPowerAutoPowerOff = ADC_AUTOPOWEROFF_DISABLE;
  hadc.Init.ChannelsBank = ADC_CHANNELS_BANK_A;
  hadc.Init.ContinuousConvMode = DISABLE;
  hadc.Init.NbrOfConversion = 1;
  hadc.Init.DiscontinuousConvMode = DISABLE;
  hadc.Init.ExternalTrigConv = ADC_SOFTWARE_START;
  hadc.Init.ExternalTrigConvEdge = ADC_EXTERNALTRIGCONVEDGE_NONE;
  hadc.Init.DMAContinuousRequests = DISABLE;
  if (HAL_ADC_Init(&hadc) != HAL_OK)
  {
    Error_Handler();
  }
  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time. 
  */
  sConfig.Channel = ADC_CHANNEL_TEMPSENSOR;
  sConfig.Rank = ADC_REGULAR_RANK_1;
  sConfig.SamplingTime = ADC_SAMPLETIME_4CYCLES;
  if (HAL_ADC_ConfigChannel(&hadc, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN ADC_Init 2 */
  ADC_ChannelConfTypeDef sConfig2 = {0};
   hadc2.Instance = ADC1;
   hadc2.Init.ClockPrescaler = ADC_CLOCK_ASYNC_DIV1;
   hadc2.Init.Resolution = ADC_RESOLUTION_12B;
   hadc2.Init.DataAlign = ADC_DATAALIGN_RIGHT;
   hadc2.Init.ScanConvMode = ADC_SCAN_DISABLE;
   hadc2.Init.EOCSelection = ADC_EOC_SINGLE_CONV;
   hadc2.Init.LowPowerAutoWait = ADC_AUTOWAIT_DISABLE;
   hadc2.Init.LowPowerAutoPowerOff = ADC_AUTOPOWEROFF_DISABLE;
   hadc2.Init.ChannelsBank = ADC_CHANNELS_BANK_A;
   hadc2.Init.ContinuousConvMode = DISABLE;
   hadc2.Init.NbrOfConversion = 1;
   hadc2.Init.DiscontinuousConvMode = DISABLE;
   hadc2.Init.ExternalTrigConv = ADC_SOFTWARE_START;
   hadc2.Init.ExternalTrigConvEdge = ADC_EXTERNALTRIGCONVEDGE_NONE;
   hadc2.Init.DMAContinuousRequests = DISABLE;
   if (HAL_ADC_Init(&hadc2) != HAL_OK)
   {
     Error_Handler();
   }
   /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
   */
   sConfig2.Channel = ADC_CHANNEL_VREFINT;
   sConfig2.Rank = ADC_REGULAR_RANK_1;
   sConfig2.SamplingTime = ADC_SAMPLETIME_4CYCLES;
   if (HAL_ADC_ConfigChannel(&hadc2, &sConfig2) != HAL_OK)
   {
     Error_Handler();
   }
  /* USER CODE END ADC_Init 2 */

}

void MX_ADC_Init2(void)
{

  /* USER CODE BEGIN ADC_Init 0 */

  /* USER CODE END ADC_Init 0 */

  ADC_ChannelConfTypeDef sConfig = {0};

  /* USER CODE BEGIN ADC_Init 1 */

  /* USER CODE END ADC_Init 1 */
  /** Configure the global features of the ADC (Clock, Resolution, Data Alignment and number of conversion)
  */
  /* USER CODE BEGIN ADC_Init 2 */
  ADC_ChannelConfTypeDef sConfig2 = {0};
   hadc2.Instance = ADC1;
   hadc2.Init.ClockPrescaler = ADC_CLOCK_ASYNC_DIV1;
   hadc2.Init.Resolution = ADC_RESOLUTION_12B;
   hadc2.Init.DataAlign = ADC_DATAALIGN_RIGHT;
   hadc2.Init.ScanConvMode = ADC_SCAN_DISABLE;
   hadc2.Init.EOCSelection = ADC_EOC_SINGLE_CONV;
   hadc2.Init.LowPowerAutoWait = ADC_AUTOWAIT_DISABLE;
   hadc2.Init.LowPowerAutoPowerOff = ADC_AUTOPOWEROFF_DISABLE;
   hadc2.Init.ChannelsBank = ADC_CHANNELS_BANK_A;
   hadc2.Init.ContinuousConvMode = DISABLE;
   hadc2.Init.NbrOfConversion = 1;
   hadc2.Init.DiscontinuousConvMode = DISABLE;
   hadc2.Init.ExternalTrigConv = ADC_SOFTWARE_START;
   hadc2.Init.ExternalTrigConvEdge = ADC_EXTERNALTRIGCONVEDGE_NONE;
   hadc2.Init.DMAContinuousRequests = DISABLE;
   if (HAL_ADC_Init(&hadc2) != HAL_OK)
   {
     Error_Handler();
   }
   /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
   */
   sConfig2.Channel = ADC_CHANNEL_TEMPSENSOR;
   sConfig2.Rank = ADC_REGULAR_RANK_1;
   sConfig2.SamplingTime = ADC_SAMPLETIME_4CYCLES;
   if (HAL_ADC_ConfigChannel(&hadc2, &sConfig2) != HAL_OK)
   {
     Error_Handler();
   }
  /* USER CODE END ADC_Init 2 */

}

/**
  * @brief USART2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART2_UART_Init(void)
{

  /* USER CODE BEGIN USART2_Init 0 */

  /* USER CODE END USART2_Init 0 */

  /* USER CODE BEGIN USART2_Init 1 */

  /* USER CODE END USART2_Init 1 */
  huart2.Instance = USART2;
  huart2.Init.BaudRate = 350000;
  huart2.Init.WordLength = UART_WORDLENGTH_8B;
  huart2.Init.StopBits = UART_STOPBITS_1;
  huart2.Init.Parity = UART_PARITY_NONE;
  huart2.Init.Mode = UART_MODE_TX_RX;
  huart2.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart2.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART2_Init 2 */

  /* USER CODE END USART2_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

}

/* USER CODE BEGIN 4 */
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{ 
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
