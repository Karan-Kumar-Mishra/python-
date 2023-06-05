from win32com.client import Dispatch
speak=Dispatch("SAPI.SpVoice")
s=input("Enter the string Speak =>> ")
speak.Speak(s)
