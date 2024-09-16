#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.chat.util import Chat, reflections


# In[4]:


chats = [
         ["hello", ["hi"]],
         ["my name is (.*)", ["Hi, %1"]],
         ["hi|hey|hola", ["hello"]],
         ["My city is (.*)", ["glad to know that your from %1"]],
         ["What is InfusionMedz.com?", ["InfusionMedz.com is an online pla3orm dedicated to providing medical educa8on, teleconsulta8on services, and health awareness to both medical professionals and the general public. Our aim is to enhance medical knowledge and improve healthcare accessibility."]],
         ["Who can benefit from InfusionMedz.com?", [" Our services are designed for medical students, prac8cing doctors, and anyone seeking reliable health informa8on or medical consulta8on."]],
         ["How do I sign up for services at InfusionMedz.com?", ["You can sign up through our website by clicking on the 'Register' buCon at the top of the homepage. Follow the prompts to create an account and access our services." ]],
         ["How does InfusionMedz.com help with NEET PG preparaton?", [" We offer a comprehensive NEET PG prepara8on program that includes an extensive database of MCQs, personalized one-on-one discussions, customized study schedules, targeted assistance on weaker subjects, and frequent grand tests."]],
         ["Can I schedule a one-on-one session for NEET PG preparaton?", ["Yes, you can schedule one-on-one sessions with our experts by logging into your account and selec8ng 'Schedule a Session' from your dashboard."]],
         ["How do I book a teleconsultaton at InfusionMedz.com?", ["To book a teleconsulta8on, please log into your account, navigate to the Teleconsulta8on sec8on, and select a specialist based on your health concerns. You can then choose an available 8me slot that suits your schedule."]],
         ["What kind of specialists are available for teleconsultaton?", ["We have a wide range of specialists available, including general prac88oners, cardiologists, dermatologists, pediatricians, and more."]],
         ["What types of clinical examinaton skills can I learn at InfusionMedz.com?", ["Our program covers all essen8al clinical examina8on skills, including head-to- toe assessments, system-specific examina8ons, and specialized techniques relevant to fields like cardiology, neurology, and pediatrics"]],
         ["How are the clinical skills sessions conducted?", ["Sessions are conducted online through interac8ve videos and live prac8ce sessions with feedback from experienced instructors. We also use virtual reality tools to enhance learning."]],
         ["Where can I find informaton on disease preventon and health awareness?", ["You can access a wealth of informa8on on disease preven8on, health awareness, and lifestyle modifica8ons in the Health Educa8on sec8on of our website."]],
         ["Do you provide informaton on lifestyle changes for beNer health?", ["Yes, we offer comprehensive advice on lifestyle modifica8ons that include diet, exercise, stress management, and preven8ve health prac8ces to improve overall well-being."]],
         ["How do I reset my password?", ["To reset your password, click on the 'Forgot Password' link on the login page and follow the instruc8ons to receive an email with a link to reset your password."]],
         ["Who can I contact for technical support?",["For technical support, please email our support teamat support@infusionmedz.com or use the live chat feature on our website for immediate assistance."]],
         ["What payment methods are accepted on InfusionMedz.com?", ["We accept various payment methods including credit cards, debit cards, and online banking. All transac8ons are secure and encrypted."]],
         ["How do I cancel my subscripton?", ["You can cancel your subscrip8on at any 8me by accessing your account seWngs and selec8ng the 'Cancel Subscrip8on' op8on. If you need assistance, please contact our customer service."]],
         ["Can I access the educational materials offline?", ["Currently, our educa8onal materials need an internet connec8on for access. However, you can save certain resources for offline study as indicated on our pla3orm."]],
         ["Are there any free trial periods for your educatonal programs?", ["Yes, we offer a 7-day free trial for new users to explore our educa8onal programs. You can sign up without any obliga8on and cancel any8me during the trial period."]],
         ["Can I get medical advice for specific symptoms through the chatbot?", ["For specific medical advice, it's best to book a teleconsulta8on with one of our specialists who can provide you with personalized care. Our chatbot is designed to guide you to the right services on our pla3orm."]],
         ["What should I do in case of a medical emergency?", ["In case of a medical emergency, please contact local emergency services immediately. Our pla3orm is not a subs8tute for urgent medical care."]],
         ["How can I collaborate with InfusionMedz.com?", ["For collabora8on inquiries, please contact us at partnerships@infusionmedz.com. We are always looking for opportuni8es to expand our network and improve our offerings."]],
         ["Does InfusionMedz.com offer internships or opportunities for students?", ["Yes, we offer internships and other opportuni8es for students interested in medical educa8on and digital health solu8ons. Please visit our Careers page for more informa8on and applica8on details."]],
         ["How can I provide feedback on your services?", ["We value your feedback! Please visit the Feedback sec8on on our website or click on the 'Give Feedback' buCon in your user dashboard to share your thoughts and sugges8ons"]],
         ["What if I experience issues during a live session or webinar?", ["If you experience any issues during a live session or webinar, please use the 'Report Issue' buCon available during the event or contact our technical support team directly for immediate assistance."]],
         ["How oTen are the NEET PG preparaton materials updated?", ["Our NEET PG prepara8on materials are updated annually to reflect the latest exam paCerns and guidelines. We also periodically add new ques8ons and resources based on recent exams and student feedback."]],
         ["What are the qualificatons of the doctors providing teleconsultatons?", ["All doctors on our pla3orm are cer8fied and have extensive experience in their respec8ve fields. You can view detailed profiles, including qualifica8ons and areas of specialty, before booking a consulta8on."]],
         ["How does InfusionMedz.com ensure the privacy and security of my medical informaton?",["We adhere to strict privacy and data protec8on laws. All personal and medical informa8on is encrypted and stored securely. For more details, you can view our Privacy Policy on our website."]],
         ["What safety measures are in place for online consultatons during the COVID-19 pandemic?",["During the COVID-19 pandemic, all our services are designed to minimize risk by providing remote access to healthcare and maintaining the highest standards of safety during online consulta8ons and follow-ups."]],
         ["Does InfusionMedz.com offer certficates for completed courses or programs?",["Yes, we provide cer8ficates of comple8on for various educa8onal programs and courses. These cer8ficates can be downloaded directly from your account once you meet all the program requirements."]],
         ["Can I use the educatonal courses for contnuing medical educaton (CME) credits?",["Several of our courses are eligible for CME credits. Please check the course details for specific CME eligibility and how to apply these credits towards your professional requirements."]],
         ["Is the website accessible to people with disabilites?",["Yes, our website is designed to be accessible to individuals with disabili8es. We adhere to ADA standards to ensure that everyone can navigate and benefit from our services effec8vely."]],
         ["What languages are supported by InfusionMedz.com?",["Currently, our primary language of instruc8on and support is English. We are working to include mul8ple languages in the future to cater to a broader audience."]]
]         


# In[5]:


chat = Chat(chats, reflections)


# In[ ]:


chat.converse()


# In[ ]:




