from mycroft import MycroftSkill, intent_file_handler


class RivalMouseVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voice.mouse.rival.intent')
    def handle_voice_mouse_rival(self, message):
        self.speak_dialog('voice.mouse.rival')


def create_skill():
    return RivalMouseVoice()

