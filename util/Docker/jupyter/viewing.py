from IPython.display import display
import ipywidgets as widgets


def create_dropdown_values(array):
    '''
    Create a dropdown with the added items
    Ninguno and Todos.
    '''
    dd = list(set(array))
    dd.sort()
    dd = ['Ninguno', 'Todos'] + dd
    return dd


def generate_simple_eventhandler(output, df, col):
    '''Generate a simple eventhandler which compares values.'''
    def event_handler(change):
        output.clear_output()
        with output:
            if (change.new == 'Ninguno'):
                output.clear_output()
            elif (change.new == 'Todos'):
                display(df)
            else:
                display(df[df[col] == change.new])

    return event_handler
