import argparse
from InquirerPy import prompt, inquirer

def _parse_arguments(args_as_list=None):
  """Function which parses arguments from stdin (or list of args).

  :param args_as_list: When set, parser reads from `args_as_list` and not stdin, defaults to None
  :type args_as_list: List of string, optional


  E.g. `args_as_list` can be provided to run the parser from other Python code.
  # from shell:
  python main.py -s Hello -n 100 -b -l 1 10 2
  
  # or from other Python code:
  _parse_arguments(
    ['-s', 'Hello', '-n', '100', '-b', '-l', '1', '10', '2']
  )

  :return: Dictionary of arguments
  :rtype: Dict
  """

  # Instantiate argparser
  parser = argparse.ArgumentParser(
    description="Put your description here"
  )

  # Add arguments
  parser.add_argument(
    "--string-arg", "-s",
    default=["Howdy"],
    help="String argument.",
    type=str, nargs=1
  )
  parser.add_argument(
    "--number_arg",
    "-n",
    default=[0],
    help="Integer argument.",
    type=int, nargs=1
  )
  parser.add_argument(
    "--list_arg", "-l",
    default=[1,2,3,4],
    help="A list of ints",
    type=int,
    nargs='+' # use nargs='+' to require at least one value
  )  
  parser.add_argument(
    "--bool_arg","-b",
    default=False,
    help="Boolean argument.",
    action="store_true"
  )

  # Parse and access arguments
  # string and numbers are stored in lists, bools are not
  if args_as_list is None:
    args = parser.parse_args()
  else:
    args = parser.parse_args(args_as_list)
  
  return {
    "string_arg" : args.string_arg[0],
    "number_arg" : args.number_arg,
    "list_arg"   : args.list_arg,
    "bool_arg"   : args.bool_arg
  }

def main(string_arg, number_arg, list_arg, bool_arg):
  """
  Main simply prints its arguments.
  """
  """[Summary]

  :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
  :type [ParamName]: [ParamType](, optional)
  ...
  :raises [ErrorType]: [ErrorDescription]
  ...
  :return: [ReturnDescription]
  :rtype: [ReturnType]
  """

  print(f"string_arg: {string_arg}")
  print(f"number_arg: {number_arg}")
  print(f"list_arg: {list_arg}")
  print(f"bool_arg: {bool_arg}")
  

if __name__ == '__main__':
  '''
  Minimal logic is kept in the top-level scope here.
  This way, the interface is kept separate and reusable or replacable,
  and the logic (`main()`) is kept separate and importable.
  '''
  args_dict = _parse_arguments()
  main(
    string_arg = args_dict["string_arg"],
    number_arg = args_dict["number_arg"],
    list_arg   = args_dict["list_arg"],
    bool_arg   = args_dict["bool_arg"]
  )