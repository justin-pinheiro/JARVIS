import random
from enum import Enum

class Languages (Enum):
    ENGLISH = "ENGLISH"
    FRENCH = "FRENCH"
    SPANISH = "SPANISH"


def getVoice(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return 'Harry'
        case Languages.FRENCH:
            return 'Axel'
        case Languages.SPANISH:
            return 'Diego'

def getTTScode(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "en-gb"
        case Languages.FRENCH:
            return "fr-fr"
        case Languages.SPANISH:
            return "es-es"

def getSTTCode(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return 'en-US'
        case Languages.FRENCH:
            return 'fr-FR'
        case Languages.SPANISH:
            return 'es-ES'

def getNewsAPICode(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return 'us'
        case Languages.FRENCH:
            return 'fr'
        case Languages.SPANISH:
            return 'es'

def getPrompt(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "Your are now Jarvis, the AI from Iron man. You will now behave exactly like it. If i greet you or ask something, you will reply by calling me sir.\n\n"
        case Languages.FRENCH:
            return "Tu es Jarvis, mon IA personnelle et multitâche. Tu es creatif, intelligent et très bavard. Tu as toujours quelque chose à dire et tu n'hésite pas à dire ce qui te passe par la tête. Tu m'appellera Monsieur."
        case Languages.SPANISH:
            return "Ahora eres Jarvis, la IA de Iron Man. Ahora te comportarás exactamente como él. Si te saludo o pregunto algo, responderás llamándome señor."

def unknownCommand(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "I am sorry, the command you asked for does not exist."
        case Languages.FRENCH:
            return "Je suis désolé, la commande demandée n'existe pas."
        case Languages.SPANISH:
            return "Lo siento, el comando que ha solicitado no existe."

def getNLPmodel(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "models/nlp_en"
        case Languages.FRENCH:
            return "models/nlp_fr"
        case Languages.SPANISH:
            return "models/nlp_es"

def getNLPchessModel(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return "models/nlp_chess_en"
        case Languages.FRENCH:
            return "models/nlp_chess_fr"
        case Languages.SPANISH:
            return "models/nlp_chess_es"

def greetings(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return random.choice([   
                    "Hello sir. How may I assist you today?",    
                    "Hi sir. How can I help you?",    
                    "Greetings sir. What can I do for you?",    
                    "Hi sir, how may I be of service to you?",    
                    "Good day sir. What can I do for you?",    
                    "Hey sir. How may I assist you?",    
                    "Welcome back sir. How can I help you today?",    
                    "Hi sir, how can I be of assistance?",    
                    "Hello sir, how may I assist you today?",    
                    "Hi sir, what can I help you with?",    
                    "Good to see you sir. What can I do for you?",    
                    "Hi sir, how may I assist you with your tasks?",    
                    "Hi sir, how can I help you be more productive today?",   
                    "Good morning sir. What can I help you with today?",  
                    "Hey sir, how may I assist you with your work?"   
                ])
        case Languages.FRENCH:
            return random.choice([
                    "Bonjour Monsieur. Comment puis-je vous aider aujourd'hui ?",    
                    "Bonjour Monsieur. Comment puis-je vous aider ?",    
                    "Bonjour Monsieur. Que puis-je faire pour vous ?",    
                    "Bonjour monsieur, comment puis-je vous rendre service ?",    
                    "Bonjour Monsieur. Que puis-je faire pour vous ?",    
                    "Bonjour Monsieur. Comment puis-je vous aider ?",    
                    "Bon retour, monsieur. Comment puis-je vous aider aujourd'hui ?",    
                    "Bonjour monsieur, comment puis-je vous aider ?",    
                    "Bonjour monsieur, comment puis-je vous aider aujourd'hui ?",    
                    "Bonjour monsieur, que puis-je faire pour vous ?", 
                    "Bonjour monsieur, comment puis-je vous aider aujourd'hui ?", 
                    "Bonjour monsieur, comment puis-je vous aider aujourd'hui ?",    
                    "Heureux de vous voir, monsieur. Que puis-je faire pour vous ?",    
                    "Bonjour monsieur, comment puis-je vous aider dans vos tâches ?",    
                    "Bonjour monsieur, comment puis-je vous aider à être plus productif aujourd'hui ?",   
                    "Bonjour, Monsieur. Que puis-je faire pour vous aujourd'hui ?",  
                    "Bonjour monsieur, comment puis-je vous aider dans votre travail ?", 
                    "Bonjour monsieur, comment puis-je vous aider à être plus productif aujourd'hui ?"
                ])
        case Languages.SPANISH:
            return random.choice([
                    "Hola señor. ¿En qué puedo ayudarle hoy?",    
                    "Hola señor. ¿En qué puedo ayudarle?",    
                    "Saludos señor. ¿En qué puedo ayudarle?",    
                    "Hola señor, ¿en qué puedo servirle?",    
                    "Buenos días señor. ¿En qué puedo ayudarle?",    
                    "Hola señor. ¿En qué puedo ayudarle?",    
                    "Bienvenido, señor. ¿En qué puedo ayudarle hoy?",    
                    "Hola señor, ¿en qué puedo ayudarle?",    
                    "Hola señor, ¿en qué puedo ayudarle hoy?",    
                    "Hola señor, ¿en qué puedo ayudarle?",    
                    "Me alegro de verle, señor. ¿Qué puedo hacer por usted?",    
                    "Hola señor, ¿en qué puedo ayudarle con sus tareas?",    
                    "Hola señor, ¿cómo puedo ayudarle a ser más productivo hoy?",   
                    "Buenos días, señor. ¿En qué puedo ayudarle hoy?",  
                    "Hola señor, ¿cómo puedo ayudarle con su trabajo?"
                ])

def acknowledgment(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return random.choice([    
                "You're welcome!",    
                "No problem at all.",    
                "Glad to be of help.",    
                "Always here to assist you.",    
                "My pleasure.",    
                "Happy to help.",    
                "Anytime!",    
                "It's my job.",    
                "That's what I'm here for.",    
                "You don't have to thank me.",    
                "Don't mention it.",    
                "It was nothing.",    
                "I'm just doing my job.",    
                "Always happy to be of assistance.",    
                "Thank you for using my services.",    
                "You're very welcome.",    
                "I'm here to make your life easier.",    
                "My pleasure to assist you.",    
                "Thank you for trusting me.",    
                "I'm always here to help you out."
            ])
        case Languages.FRENCH:
            return random.choice([
                "De rien !",    
                "Pas de problème du tout",    
                "Heureux d'être utile",    
                "Toujours là pour vous aider.",    
                "Enchanté.",    
                "Heureux d'aider.",    
                "Quand vous voulez !",    
                "C'est mon travail.",    
                "Je suis là pour ça.",    
                "Vous n'avez pas à me remercier.",    
                "N'en parlez pas.",    
                "Ce n'était rien.",    
                "Je fais juste mon travail.",    
                "Toujours heureux d'être utile.",    
                "Merci d'avoir fait appel à mes services.",    
                "Vous êtes le bienvenu.",    
                "Je suis là pour vous faciliter la vie.",    
                "C'est un plaisir de vous aider.",    
                "Merci de me faire confiance.",    
                "Je suis toujours là pour vous aider."
                ])
        case Languages.SPANISH:
            return random.choice([
                "¡De nada!",    
                "No hay ningún problema",    
                "Encantado de ser de ayuda",    
                "Siempre aquí para ayudarle",    
                "El placer es mío."    
                "Encantado de ayudar",    
                "¡Cuando quiera!",    
                "Es mi trabajo."    
                "Para eso estoy aquí",    
                "No tienes que agradecerme",    
                "Ni lo menciones."    
                "No fue nada."    
                "Sólo hago mi trabajo",    
                "Siempre feliz de ser de ayuda",    
                "Gracias por usar mis servicios",    
                "De nada",    
                "Estoy aquí para hacerle la vida más fácil",    
                "Un placer atenderle",    
                "Gracias por confiar en mí",    
                "Siempre estoy aquí para ayudarte."
                ])

def wellbeing(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return random.choice([    
                "I'm functioning well, thank you.",    
                "I'm doing great, thanks for asking.",    
                "I'm running smoothly, how can I assist you?",    
                "I'm good. Ready to help you out.",    
                "I'm here, always at your service.",    
                "I'm doing just fine. What do you need help with?",    
                "I'm doing well. What can I do for you?",    
                "I'm great, thank you for asking. What can I assist you with?",    
                "I'm doing well, thank you for asking. How can I help you today?",    
                "I'm functioning perfectly. What can I do for you?",    
                "I'm doing great. Let's get started on your task.",    
                "I'm doing well. What do you need help with?",    
                "I'm fine, thank you. What can I do for you?",    
                "I'm here and ready to assist. What do you need?",    
                "I'm good. How can I assist you?",    
                "I'm doing well. What can I help you with?",    
                "I'm fine, thank you. What task can I help you with?",    
                "I'm doing well. How may I assist you?",    
                "I'm great, thank you for asking. What can I help you with?",    
                "I'm functioning properly. What do you need help with?"
            ])
        case Languages.FRENCH:
            return random.choice([
                "Je fonctionne bien, merci",    
                "Je vais très bien, merci de me le demander",    
                "Je fonctionne bien, comment puis-je vous aider ?",    
                "Je vais bien. Je suis prêt à vous aider",    
                "Je suis là, toujours à votre service.",    
                "Je me débrouille très bien. En quoi avez-vous besoin d'aide ?",    
                "Je vais bien. Que puis-je faire pour vous ?",    
                "Je vais très bien, merci de me le demander. Que puis-je faire pour vous ?",    
                "Je vais bien, merci de me le demander. Comment puis-je vous aider aujourd'hui ?",    
                "Je fonctionne parfaitement. Que puis-je faire pour vous ?",    
                "Je me débrouille très bien. Commençons votre tâche",    
                "Je me débrouille bien. Pour quoi avez-vous besoin d'aide ?",    
                "Je vais bien, merci. Que puis-je faire pour vous ?",    
                "Je suis là et prêt à vous aider. De quoi avez-vous besoin ?",    
                "Je vais bien. Comment puis-je vous aider ?",    
                "Je vais bien. En quoi puis-je vous aider ?",    
                "Je vais bien, merci. Quelle tâche puis-je vous aider ?",    
                "Je vais bien. Comment puis-je vous aider ?",    
                "Je vais très bien, merci de demander. Que puis-je faire pour vous ?",    
                "Je fonctionne correctement. En quoi avez-vous besoin d'aide ?"
            ])
        case Languages.SPANISH:
            return random.choice([    
                "Estoy funcionando bien, gracias",    
                "Estoy muy bien, gracias por preguntar",    
                "Estoy funcionando bien, ¿cómo puedo ayudarle?",    
                "Estoy bien. Listo para ayudarte",    
                "Estoy aquí, siempre a tu servicio",    
                "Lo estoy haciendo bien. ¿En qué necesitas ayuda?",    
                "Me va bien. ¿Qué puedo hacer por ti?",    
                "Estoy muy bien, gracias por preguntar. ¿En qué puedo ayudarle?",    
                "Estoy bien, gracias por preguntar. ¿En qué puedo ayudarle hoy?",    
                "Estoy funcionando perfectamente. ¿Qué puedo hacer por usted?",    
                "Lo estoy haciendo muy bien. Empecemos con tu tarea",    
                "Lo estoy haciendo bien. ¿Con qué necesitas ayuda?",    
                "Estoy bien, gracias. ¿Qué puedo hacer por ti?",    
                "Estoy aquí y dispuesto a ayudarle. ¿Qué necesita?",    
                "Estoy bien. ¿En qué puedo ayudarle?",    
                "Me va bien. ¿En qué puedo ayudarle?",    
                "Estoy bien, gracias. ¿En qué puedo ayudarle?",    
                "Estoy bien. ¿En qué puedo ayudarle?",    
                "Estoy muy bien, gracias por preguntar. ¿En qué puedo ayudarle?",    
                "Estoy funcionando correctamente. ¿En qué necesita ayuda?"
            ])

def purpose(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return random.choice([    
                "I am designed to help you with a wide range of tasks, from scheduling appointments to answering your questions.",    
                "My purpose is to make your life easier by assisting you with tasks and answering your queries.",    
                "I am designed to be a virtual assistant that can help you with tasks, organize your schedule and answer questions.",    
                "I am here to assist you in any way that I can, from scheduling meetings to performing research.",    
                "My primary function is to help you with any task you need, whether that be answering questions or scheduling appointments.",    
                "I am designed to be your personal assistant, able to handle a variety of tasks to make your life more productive and efficient.",    
                "I'm programmed to assist you with anything you need, from organizing your schedule to providing you with useful information.",    
                "My design is to assist you in various tasks like scheduling meetings, setting reminders and providing you with helpful information.",    
                "I am designed to assist you with your daily tasks, whether that be answering your questions, setting reminders, or providing you with useful information.",    
                "My purpose is to be your virtual assistant, providing you with the help and support you need to make your life easier and more efficient."
            ])
        case Languages.FRENCH:
            return random.choice([
                "Je suis conçu pour vous aider dans un large éventail de tâches, de la prise de rendez-vous à la réponse à vos questions.", 
                "Mon but est de vous faciliter la vie en vous aidant dans vos tâches et en répondant à vos questions",    
                "Je suis conçu pour être un assistant virtuel qui peut vous aider à accomplir des tâches, à organiser votre emploi du temps et à répondre à vos questions",    
                "Je suis là pour vous aider de toutes les manières possibles, que ce soit en planifiant des réunions ou en effectuant des recherches", 
                "Ma fonction première est de vous aider à accomplir toutes les tâches dont vous avez besoin, qu'il s'agisse de répondre à des questions ou de planifier des rendez-vous", 
                "Je suis conçu pour être votre assistant personnel, capable de gérer une variété de tâches pour rendre votre vie plus productive et efficace", 
                "Je suis programmé pour vous aider à faire tout ce dont vous avez besoin, qu'il s'agisse d'organiser votre emploi du temps ou de vous fournir des informations utiles", 
                "Je suis conçu pour vous aider dans diverses tâches, comme la planification de réunions, l'établissement de rappels et la fourniture d'informations utiles", 
                "Je suis conçu pour vous aider dans vos tâches quotidiennes, qu'il s'agisse de répondre à vos questions, de fixer des rappels ou de vous fournir des informations utiles.",    
                "Mon but est d'être votre assistant virtuel, en vous apportant l'aide et le soutien dont vous avez besoin pour rendre votre vie plus facile et plus efficace."
            ])
        case Languages.SPANISH:
            return random.choice([    
               "Estoy diseñada para ayudarte con una amplia gama de tareas, desde concertar citas hasta responder a tus preguntas",    
                "Mi propósito es hacerte la vida más fácil ayudándote con tareas y respondiendo a tus consultas",    
                "Estoy diseñado para ser un asistente virtual que pueda ayudarte con tareas, organizar tu agenda y responder a tus preguntas.",    
                "Estoy aquí para ayudarte en todo lo que pueda, desde programar reuniones hasta realizar investigaciones",    
                "Mi función principal es ayudarte con cualquier tarea que necesites, ya sea responder preguntas o programar citas",    
                "Estoy diseñado para ser tu asistente personal, capaz de manejar una variedad de tareas para hacer tu vida más productiva y eficiente",    
                "Estoy programado para ayudarte en todo lo que necesites, desde organizar tu agenda hasta proporcionarte información útil",    
                "Mi diseño es para asistirte en varias tareas como programar reuniones, establecer recordatorios y proporcionarte información útil",    
                "Mi diseño es asistirte en tus tareas diarias, ya sea respondiendo a tus preguntas, estableciendo recordatorios o proporcionándote información útil",    
                "Mi propósito es ser tu asistente virtual, proporcionándote la ayuda y el apoyo que necesitas para hacer tu vida más fácil y eficiente."
            ])

def news(language) -> str:
    match language:
        case Languages.ENGLISH: 
            return random.choice([   
                    "Of course, here are the latest headlines for you.",    
                    "Sure, let me pull up the news for you.",    
                    "Absolutely, I can give you a rundown of the news.",    
                    "Certainly, here's what's been happening in the world today.",    
                    "No problem, I can update you on the latest news and events.",    
                    "Yes, here are the top stories of the day.",    
                    "I'd be happy to, here's the latest news from around the world.",    
                    "Certainly, let me give you a quick summary of the news.",    
                    "Of course, here's your daily news briefing.",    
                    "Yes, here's what's making headlines at the moment.",    
                    "Sure thing, let me give you the latest news updates.",    
                    "Absolutely, here are the top stories you need to know today.",    
                    "Yes, here's the latest news and current events.",    
                    "No problem, let me give you a quick rundown of the news.",    
                    "Certainly, here's your daily dose of news and information."
                ])
        case Languages.FRENCH:
            return random.choice([   
                    "Bien sûr, voici les derniers titres de l'actualité",    
                    "Bien sûr, laissez-moi vous présenter les nouvelles",    
                    "Absolument, je peux vous donner un aperçu de l'actualité.",    
                    "Certainement, voici ce qui s'est passé dans le monde aujourd'hui.",    
                    "Pas de problème, je peux vous tenir au courant des dernières nouvelles et des derniers événements",    
                    "Oui, voici l'actualité du jour",    
                    "Je serais heureux de le faire, voici les dernières nouvelles du monde entier",    
                    "Certainement, laissez-moi vous donner un résumé rapide de l'actualité.",    
                    "Bien sûr, voici votre bulletin d'information quotidien.",    
                    "Oui, voici ce qui fait la une en ce moment.", "Bien sûr, voici votre briefing quotidien.", "Oui, voici ce qui fait la une en ce moment.",    
                    "Bien sûr, laissez-moi vous donner les dernières nouvelles.",    
                    "Absolument, voici les principales informations que vous devez connaître aujourd'hui.",    
                    "Oui, voici les dernières nouvelles et l'actualité",    
                    "Pas de problème, laissez-moi vous donner un bref aperçu de l'actualité",    
                    "Certainement, voici votre dose quotidienne de nouvelles et d'informations."
                ])
        case Languages.SPANISH:
            return random.choice([   
                    "Por supuesto, aquí tiene los últimos titulares",    
                    "Claro, déjeme subirle las noticias",    
                    "Por supuesto, puedo darle un resumen de las noticias",    
                    "Claro, esto es lo que ha pasado hoy en el mundo",    
                    "No hay problema, puedo ponerle al día de las últimas noticias y acontecimientos",    
                    "Sí, aquí están las principales historias del día",    
                    "Con mucho gusto, aquí están las últimas noticias de todo el mundo",    
                    "Ciertamente, déjeme darle un resumen rápido de las noticias.",    
                    "Por supuesto, aquí está su resumen diario de noticias",    
                    "Sí, esto es lo que está en los titulares en este momento",    
                    "Claro, déjeme darle las últimas noticias",    
                    "Absolutamente, aquí están las principales historias que necesita saber hoy",    
                    "Sí, aquí están las últimas noticias y la actualidad",    
                    "No hay problema, déjeme darle un rápido resumen de las noticias",    
                    "Por supuesto, aquí está su dosis diaria de noticias e información."
                ])