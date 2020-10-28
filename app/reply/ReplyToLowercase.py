import re
from random import choice

from .ReplyBase import ReplyBase

MESSAGES = [
    "NÃO TO TE OUVINDO MEU CONSAGRADO, PODE FALAR UM POUQUINHO MAIS ALTO??",
    "QUE????????????",
    "FALA MAIS ALTO NÃO TE ESCUTOOO",
    "FALANDO BAIXO ASSIM EU NÃO TE ESCUTO MEU MAGNÂNIMO",
    "PRA INTERAGIR TEM QUE GRITAR QUE ESSE ESQUELETO JÁ TÁ VELHO E SURDO",
    "VOU FINGIR QUE TE ESCUTEI MEU ARISTOCRATA",
    "PODE CHEGAR UM POUQUINHO MAIS PERTO E GRITAR NO MEU OUVIDO??",
    "TÁ COM VERGONHA?? FALA MAIS ALTO MEU SUSSURADOR!!",
    "SÓ QUERIA DUAS COISAS NESSE MUNDO: 1 (UM) QUE A MORENA ME NOTASSE E 2 (DOIS) QUE FALASSEM MAIS ALTO PRA EU CONSEGUIR ENTENDER",
    "DICA DE CÁLCIO: APERTA CAPS LOCK UMA VEZ E DEPOIS NUNCA MAIS!!",
    "VOU AUMENTAR TEU VOLUME NO AUDACITY E TE AVISO",
    "ALGUEM OUVIU ALGUMA COISA??",
    "TÁ NO TUNEL?? A LIGAÇÃO TÁ CORTANDO FALA MAIS ALTO!!!",
    "NÃO ESCUTEI MEU TREVOSO, PODE REPETIR?",
    "TÓ AQUI ESSA MEGAFONE PRA VER SE TE AJUDA, MEU MUDO 📣",
    "TIRA O COROTE DA BOCA E FALA DE NOVO",
    "PARANOIA MINHA OU ESSE DAÍ TÁ FALANDO MUITO BAIXO?",
    "EU JÁ SOU MOUCO DAÍ VC VEM E ME FALA BAIXO, AI NÃO MEU PARCEIRO",
    "ALÔ??? ALÔ? NÃO TO OUVINDO!! QUEM É?!?!!??"
]


class ReplyToLowercase(ReplyBase):
    def __init__(self, subreddit) -> None:
        self._allowed_words = [
            r"\s?r/\w+$|r/\w+\s?|\s?r/\w+",
            r"\s?u/\w+$|u/\w+\s?|\s?u/\w+",
        ]
        super().__init__(subreddit)

    def _reply(self, comment):
        processed_body = self._remove_allowed_words(comment.body)
        if not self._is_uppercase(processed_body):
            print("Replying...")
            message = self._get_random_message()
            comment.reply(message)
        else:
            print("OK")

    def _remove_allowed_words(self, text: str):
        """Remove words that are allowed to be lowercase

        Args:
            text (str): String to remove words from

        Returns:
            # str: String without the allowed lowercase words
        """
        for allowed_word in self._allowed_words:
            text = re.sub(rf"{allowed_word}", "", text)

        return text

    @staticmethod
    def _is_uppercase(text: str):
        """Check if some string is not all uppercase

        Args:
            text (str): String to check

        Returns:
            bool: True if string is ALL uppercase. Otherwise False
        """
        # TODO: Make so if the majority of the text is uppercase return True
        return text.upper() == text

    @staticmethod
    def _get_random_message():
        return choice(MESSAGES)
