#import googletrans
#print(googletrans.LANGUAGES)


from googletrans import Translator
 
 
text1 = "Hello welcome to my website!" 
translator = Translator()
trans1 = translator.translate(text1, src='en', dest='ja')
print("English to Japanese: ", trans1.text)
