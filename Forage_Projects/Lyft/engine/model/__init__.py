from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class CarFactory(Calliope, Glissade, Palindrome, Rorschach, Thovex):
    def needs_service(self):
        if Calliope.needs_service(self) and \
                Glissade.needs_service(self) and \
                Palindrome.needs_service(self) and \
                Rorschach.needs_service(self) and \
                Thovex.needs_service(self):
            return True
        else:
            return False
