import argparse
from InquirerPy import prompt, inquirer
import InquirerPy

# todo: consider defining a dataclass or dict
# i.e. a struct which will hold arguments
# (_parse_arguments --> interactive_args --> main)

# _parse_arguments --> _interactive_args --> main

# Example of just using ArgParse
def _parse_arguments(args_as_list=None):
  """Method which parses arguments from stdin (or list of args).

  :param args_as_list: When set, parser reads from `args_as_list` and not stdin,
  defaults to None
  :type args_as_list: List of string, optional
  :return: Dictionary of arguments
  :rtype: Dict
  """

  # Instantiate argparser
  parser = argparse.ArgumentParser(
    description="Put your description here, todo"
  )

  # Add arguments, todo
  # avoid default, so _interactive_args can prompt user
  #parser.add_argument(
  #  "--customer", "-c",
  #  help="Name of the customer",
  #  type=str, nargs=1
  #)

  # Parse and access arguments
  if args_as_list is None:
    args = parser.parse_args()
  else:
    args = parser.parse_args(args_as_list)
  
  # todo: populate args dict. (or, consider using a dataclass)
  raise NotImplementedError

def _interactive_args(
  # todo: args dict (or consider a dataclass)
):
  """Function which prompts user interactively for arguments.

  If any parameter is provided, the user will not be prompted for that parameter.
  
  [Summary]

  :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
  :type [ParamName]: [ParamType](, optional)
  ...
  :raises [ErrorType]: [ErrorDescription]
  ...
  :return: [ReturnDescription]
  :rtype: [ReturnType]
  """
  
  # todo: take in args dict (or dataclass)
  # populate 'None' values using inquirer
  # then return updated args dict (or dataclass)
  raise NotImplementedError


def main(
  # todo: args dict (or consider a dataclass)
):
  """[Summary]

  :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
  :type [ParamName]: [ParamType](, optional)
  ...
  :raises [ErrorType]: [ErrorDescription]
  ...
  :return: [ReturnDescription]
  :rtype: [ReturnType]
  """
  raise NotImplementedError
  

if __name__ == '__main__':
  args_from_argparse = _parse_arguments()

  args_from_interactive = _interactive_args(
    # todo: pass args from argparse here
    # if none, prompt interactively
  )

  main(
    # todo: pass args from interactive here
  )

  # if args is provided as a dataclass, you can nest these:
  # main(_args_from_interactive(_parse_arguments()))
