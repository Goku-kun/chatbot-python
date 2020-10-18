import re, webbrowser, sys

class WindowsBot:
      
      negative_responses = ["no", "don't", "nope", "bye", "nothing", "nada", "nein", "iiye"]
      exit_commands = ["bye", "goodbye", "leave", "stop", "later", "quit", "pause", "no", "don't", "nope", "bye", "nothing", "nada", "nein", "iiye"]

      def __init__(self):
            self.intent_dictionary = {"play_music_on_youtube": [r".*play.*song.*called ([\w ]+)", r".*play.*song.*name.? ([\w ]+)", r".*play ([\w ]+)"]}

      def welcome(self):
            
            name = input("Hello, I'm the windows personal bot. Before, I can help you, I will need some information from you. What is your name?\n=>")

            help_req = input("Alright, {}! The services that I currently provide are:\n\
1. Play music on youtube. \n\
So, how can I help you?\n=>".format(name))
            
            if help_req in self.negative_responses:
                  print("Okay, I shall take my leave then. Itsureshimasu.")
                  sys.exit(0)
            
            self.conversation_handler(help_req)
      
      def conversation_handler(self, help_req):
            while not (self.leave(help_req)):
                  help_req = self.match_intent(help_req)
            sys.exit(0)
      
      def leave(self, help_req):
            for exit_command in self.exit_commands:
                  if exit_command in help_req:
                        print("I'm leaving. See you again!")
                        return True
            return False
      
      def match_intent(self, help_req):
            for key, values in self.intent_dictionary.items():
                  for regex in values:
                        found_match = re.match(regex, help_req)

                        if found_match and key == "play_music_on_youtube":
                              return self.play_music_on_youtube(found_match.groups()[0])

            return input("I'm sorry. I don't understand you. Could you request in another way? Onegaishimasu.\n=>")

      def play_music_on_youtube(self, entity):
            list_entity = entity.split()
            if (len(list_entity) == 1):
                  webbrowser.open("https://www.youtube.com/results?search_query={}".format(list_entity), new=2)
                  return input("Your searched music shall open in your default browser. Is there anything else you shall like my help with?\n=>")
            else:
                  search_query = "+".join(list_entity)
                  webbrowser.open("https://www.youtube.com/results?search_query={}".format(search_query), new=2)
                  return input("Your searched music shall open in your default browser. Is there anything else you shall like my help with?\n=>")

WindowsBotInstance = WindowsBot()
WindowsBotInstance.welcome()
