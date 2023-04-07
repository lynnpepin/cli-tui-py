import argparse
from InquirerPy import prompt, inquirer
import InquirerPy

# Example of just using ArgParse
def _parse_arguments(args_as_list=None):
  """Method which parses arguments from stdin (or list of args).

  :param args_as_list: When set, parser reads from `args_as_list` and not stdin,
  defaults to None
  :type args_as_list: List of string, optional

  E.g. `args_as_list` can be provided to run the parser from other Python code.
  # from shell:
  python main.py -c Hello -k 6 -b -l 1 10 2
  
  # or from other Python code:
  _parse_arguments(
    ['-c', 'Hello', '-k', '6', '-b', '-l', '1', '10', '2']
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
    "--customer", "-c",
    help="Name of the customer",
    type=str, nargs=1
  )
  parser.add_argument(
    "--kinsey", "-k",
    help="Score on the Kinsey scale",
    type=int, nargs=1
  )
  parser.add_argument(
    "--pronouns", "-p",
    default=["they/them"],
    help="List pronouns you use",
    type=str,
    nargs='+' # use nargs='+' to require at least one value
  )  
  parser.add_argument(
    "--activate","-a",
    default=None, # explicitly default to None, else defaults to False
    help="If set, activates your profile.",
    action="store_true"
  )

  # Parse and access arguments
  # string and numbers are stored in lists, bools are not
  if args_as_list is None:
    args = parser.parse_args()
  else:
    args = parser.parse_args(args_as_list)
  
  return {
    "customer": args.customer[0] if args.customer else None,
    "kinsey":   args.kinsey[0]   if args.kinsey   else None,
    "pronouns": args.pronouns    if args.pronouns else None,
    "activate": args.activate    if args.activate is not None else None,
    # "if x else None" is shorthand for "if x is not None else None",
    # except when x might be boolean False, such as in the case of activate
  }

def _interactive_args(
  customer=None,
  kinsey=None,
  pronouns=None,
  activate=None
):
  """Prompt user interactively for arguments.

  If any parameter is provided, the user will not be prompted for that parameter.

  :param customer: Name of the customer, defaults to None
  :type customer: str, optional
  :param kinsey: Score on the Kinsey scale, defaults to None
  :type kinsey: int, optional
  :param pronouns: List pronouns you use, defaults to None
  :type pronouns: List of str, optional
  :param activate: If set, activates your profile, defaults to None
  :type activate: bool, optional

  :return: Dictionary of arguments, see _parse_arguments
  :rtype: Dict
  """
  output = {}

  output["customer"] = (
    inquirer.text(
      message = "What is your name?",
      instruction = "(enter here):",
      long_instruction = "Type some text and press enter!",
      default = "Jude Harley"
    ).execute()
    if customer is None
    else customer
  )

  output["kinsey"] = (
    int(
      inquirer.number(
        message = "What is your Kinsey score?",
        instruction = "(pick a number):",
        long_instruction = "It's just your score!",
        validate = lambda x: (int(x) >= -1 and int(x) <= 7),
        # or use min_allowed, max_allowed
        default = 6,
      ).execute()
    )
    if kinsey is None
    else kinsey
  )

  output["pronouns"] = (
    inquirer.checkbox(
      message = "What pronouns do you use?",
      instruction = "(pick some):",
      long_instruction = "Pick some pronouns!",
      choices = [
        "he/him",
        "she/her",
        {"name": "they/them (plural)", "value": "they/them (pl)"},
        {"name": "they/them (singular)", "value": "they/them (sg)"},
      ],
    ).execute()
    if pronouns is None
    else pronouns
  )

  output["activate"] = (
    inquirer.confirm(
      message = "Do you want to activate your profile?",
      instruction = "(y/n):",
      long_instruction = "Type y or n and press enter!",
      default = True
    ).execute()
    if activate is None
    else activate
  )

  return output



def main(customer, kinsey, pronouns, activate):
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
  print(f"customer: {customer}")
  print(f"kinsey: {kinsey}")
  print(f"pronouns: {pronouns}")
  print(f"activate: {activate}")
  

if __name__ == '__main__':
  '''
  Minimal logic is kept in the top-level scope here.
  This way, the interface is kept separate and reusable or replacable,
  and the logic (`main()`) is kept separate and importable.
  '''
  args_from_argparse = _parse_arguments()

  args_from_interactive = _interactive_args(
    customer = args_from_argparse["customer"],
    kinsey   = args_from_argparse["kinsey"],
    pronouns = args_from_argparse["pronouns"],
    activate = args_from_argparse["activate"]
  )

  main(
    customer = args_from_interactive["customer"],
    kinsey   = args_from_interactive["kinsey"],
    pronouns = args_from_interactive["pronouns"],
    activate = args_from_interactive["activate"]
  )