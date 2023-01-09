from mycroft import MycroftSkill, intent_file_handler


class NusIssHelper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helper.iss.nus.intent')
    def handle_helper_iss_nus(self, message):
        self.speak_dialog('helper.iss.nus')


def create_skill():
    return NusIssHelper()

