import time
import telebot

TOKEN = "your bot token "
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Welcome to ElectroBot... type /list to go further')

@bot.message_handler(commands=['help']) # help message handler
def send_help(message):
    bot.reply_to(message, '/start to start the electroBot, /list to know the Electrobot can do ')



#....................List comd handing part................................................. 
@bot.message_handler(commands=['list']) # list message handler
def send_list(message):
    bot.reply_to(message,( '/syllabus To get Syllabus \n' '/1st_sem Notes and Details\n' '/2nd_sem Notes and Details\n' 
                            '/3rd_sem Notes and Details\n' '/4th_sem Notes and Details\n' 
                            '/5th_sem Notes and Details\n' '/6th_sem Notes and Details\n' 
                            '/7th_sem Notes and Details\n' '/8th_sem Notes and Details\n '))
#........................................................................................

#....................syllabus handing part................................................. 
@bot.message_handler(commands=['syllabus']) # syllabus message handler
def send_syllabus(message):
    bot.reply_to(message, ('https://vtu.ac.in/pdf/2014syll/eee.pdf'))
 #........................................................................................

 #....................1ST SEM data handing part................................................. 
@bot.message_handler(commands=['1st_sem']) # syllabus message handler
def send_1th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 1st sem BEE. '))
    bot.reply_to(message, ('/qp1 For question papers\n' '/notes1 For module wise Notes\n '))
@bot.message_handler(commands=['qp1']) # qp message handler
def send_1th_semq(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['notes1']) # notes message handler
def send_1th_semn(message):
    bot.reply_to(message, ('/sem1_module1\n' '/sem1_module2\n' '/sem1_module3\n' '/sem1_module4\n' '/sem1_module5\n' ))
@bot.message_handler(commands=['sem1_module1'])# syllabus message handler
def send_module1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem1_module2'])# syllabus message handler
def send_module2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem1_module3'])# syllabus message handler
def send_module3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem1_module4'])# syllabus message handler
def send_module4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem1_module5'])# syllabus message handler
def send_module5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
#...............................................................................................................................




#........................2nd sem handler........................................................................................
@bot.message_handler(commands=['2nd_sem']) # 2sem message handler
def send_2nd_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 2nd sem. '))
    bot.reply_to(message, ('/qp2 For question papers\n' '/notes2 For module wise Notes\n '))
@bot.message_handler(commands=['qp2']) # qp message handler
def send_2th_semq(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['notes2']) # notes message handler
def send_2th_semn(message):
    bot.reply_to(message, ('/sem2_module1\n' '/sem2_module2\n' '/sem2_module3\n' '/sem2_module4\n' '/sem2_module5\n'))
@bot.message_handler(commands=['sem2_module1'])# module1 message handler
def send_1module1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem2_module2'])# module2 message handler
def send_1module2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem2_module3'])# module3 message handler
def send_1module3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem2_module4'])# module4 message handler
def send_1module4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['sem2_module5'])# module5 message handler
def send_1module5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
#...................................................................................................





#.................... 3rd SEM data handing part..................................................... 

@bot.message_handler(commands=['3rd_sem']) # syllabus message handler
def send_3th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details Notes and QP for 3rd sem. '))
    bot.reply_to(message, ('Select the subjects '))
    bot.reply_to(message, ('/18EE32_ECA\n''/18EE33_TG\n' '/18EE34_AE\n' '/18EE35_DSD\n' '/18EE36_EEM\n'))

#........................................................................................................... 
   
@bot.message_handler(commands=['18EE32_ECA']) # 18EE32 ECA message handler
def send_3th_semECA(message):
    bot.reply_to(message, (' ELECTRIC CIRCUIT ANALYSIS '))
    bot.reply_to(message, ('/QPECA For question papers\n' '/NotesECA For module wise Notes\n '))
@bot.message_handler(commands=['QPECA']) # QPECA message handler
def send_QPECA(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesECA']) # notes message handler
def send_NotesECA(message):
    bot.reply_to(message, ('/ECA_module1\n' '/ECA_module2\n' '/ECA_module3\n' '/ECA_module4\n' '/ECA_module5\n'))
@bot.message_handler(commands=['ECA_module1'])# module1 message handler
def send_ECAmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ECA_module2'])# module2 message handler
def send_ECAmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ECA_module3'])# module3 message handler
def send_ECAmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ECA_module4'])# module4 message handler
def send_ECAmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ECA_module5'])# module5 message handler
def send_ECAmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
#.........................................................................................................

@bot.message_handler(commands=['18EE33_TG']) # 18EE33 T&G message handler
def send_3th_semTG(message):
    bot.reply_to(message, (' TRANSFORMERS AND GENERATORS  '))
    bot.reply_to(message, ('/QPTG For question papers\n' '/NotesTG For module wise Notes\n '))
@bot.message_handler(commands=['QPTG']) # QPTG message handler
def send_QPTG(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesTG']) # notes message handler
def send_NotesTG(message):
    bot.reply_to(message, ('/TG_module1\n' '/TG_module2\n' '/TG_module3\n' '/TG_module4\n' '/TG_module5\n'))
@bot.message_handler(commands=['TG_module1'])# module1 message handler
def send_TGmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TG_module2'])# module2 message handler
def send_TGmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TG_module3'])# module3 message handler
def send_TGmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TG_module4'])# module4 message handler
def send_TGmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TG_module5'])# module5 message handler
def send_TGmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#............................................................................................................

@bot.message_handler(commands=['18EE34_AE']) # 18EE34 AE message handler
def send_3th_semAE(message):
    bot.reply_to(message, (' ANALOG ELECTRONIC CIRCUITS   '))
    bot.reply_to(message, ('/QPAE For question papers\n' '/NotesAE For module wise Notes\n '))
@bot.message_handler(commands=['QPAE']) # QPAE message handler
def send_QPAE(message):
    bot.reply_to(message, (' ANALOG ELECTRONIC CIRCUITS QUESTION PAPERS'))
    bot.reply_to(message, ('JAN2020 PAPER\n''Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesAE']) # notes message handler
def send_NotesAE(message):
    bot.reply_to(message, ('/AE_module1\n' '/AE_module2\n' '/AE_module3\n' '/AE_module4\n' '/AE_module5\n'))
@bot.message_handler(commands=['AE_module1'])# module1 message handler
def send_AEmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['AE_module2'])# module2 message handler
def send_AEmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['AE_module3'])# module3 message handler
def send_AEmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['AE_module4'])# module4 message handler
def send_AEmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['AE_module5'])# module5 message handler
def send_AEmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..............................................................................................................

@bot.message_handler(commands=['18EE35_DSD']) # 18EE35 DSD message handler
def send_3th_semDSD(message):
    bot.reply_to(message, (' DIGITAL SYSTEM DESIGN   '))
    bot.reply_to(message, ('/QPDSD For question papers\n' '/NotesDSD For module wise Notes\n '))
@bot.message_handler(commands=['QPDSD']) # QPAE message handler
def send_QPDSD(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesDSD']) # notes message handler
def send_NotesDSD(message):
    bot.reply_to(message, ('/DSD_module1\n' '/DSD_module2\n' '/DSD_module3\n' '/DSD_module4\n' '/DSD_module5\n'))
@bot.message_handler(commands=['DSD_module1'])# module1 message handler
def send_DSDmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSD_module2'])# module2 message handler
def send_DSDmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSD_module3'])# module3 message handler
def send_DSDmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSD_module4'])# module4 message handler
def send_DSDmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSD_module5'])# module5 message handler
def send_DSDmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
#...............................................................................................................

@bot.message_handler(commands=['18EE36_EEM']) # 18EE36 EEM message handler
def send_3th_semEEM(message):
    bot.reply_to(message, (' ELECTRICAL AND ELECTRONIC MEASUREMENTS  '))
    bot.reply_to(message, ('/QPEEM For question papers\n' '/NotesEEM For module wise Notes\n '))
@bot.message_handler(commands=['QPEEM']) # QPAE message handler
def send_QPEEM(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesEEM']) # notes message handler
def send_NotesEEM(message):
    bot.reply_to(message, ('/EEM_module1\n' '/EEM_module2\n' '/EEM_module3\n' '/EEM_module4\n' '/EEM_module5\n'))
@bot.message_handler(commands=['EEM_module1'])# module1 message handler
def send_EEMmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module2'])# module2 message handler
def send_EEMmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module3'])# module3 message handler
def send_EEMmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module4'])# module4 message handler
def send_EEMmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module5'])# module5 message handler
def send_EEMmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#................................................................................................................





 
#.................... 4th SEM data handing part................................................. 

@bot.message_handler(commands=['4th_sem']) # syllabus message handler
def send_4th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 4th sem. '))
    bot.reply_to(message, ('Select the subjects..'))
    bot.reply_to(message, ('/18EE42_PGE\n''/18EE43_TD\n' '/18EE44_EM\n' '/18EE45_EFT\n' '/18EE46_OLIC\n'))

#.................................................................................................................

@bot.message_handler(commands=['18EE42_PGE']) # 18EE42 PGE message handler
def send_3th_semPGE(message):
    bot.reply_to(message, (' POWER GENERATION AND ECONOMICS '))
    bot.reply_to(message, ('/QP_PGE For question papers\n' '/NotesPGE For module wise Notes\n '))
@bot.message_handler(commands=['QP_PGE']) # QPPGEmessage handler
def send_QPPGE(message):
    bot.reply_to(message, (' POWER GENERATION AND ECONOMICS TWO MODEL PAPERS '))
    bot.reply_to(message, ('MODEL PAPER 1\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee42-power-generation-economics-model-question-paper-1.pdf'))
    bot.reply_to(message, ('MODEL PAPER 2\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee42-power-generation-economics-model-question-paper-2.pdf'))
@bot.message_handler(commands=['NotesPGE']) # notes message handler
def send_NotesPGE(message):
    bot.reply_to(message, ('/PGE_module1\n' '/PGE_module2\n' '/PGE_module3\n' '/PGE_module4\n' '/PGE_module5\n'))
@bot.message_handler(commands=['PGE_module1'])# module1 message handler
def send_PGEmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PGE_module2'])# module2 message handler
def send_PGEmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PGE_module3'])# module3 message handler
def send_PGEmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PGE_module4'])# module4 message handler
def send_PGEmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PGE_module5'])# module5 message handler
def send_PGEmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..................................................................................................................

@bot.message_handler(commands=['18EE43_TD']) # 18EE43_TD message handler
def send_3th_semTD(message):
    bot.reply_to(message, (' TRANSMISSION AND DISTRIBUTION '))
    bot.reply_to(message, ('/QPTD For question papers\n' '/NotesTD For module wise Notes\n '))
@bot.message_handler(commands=['QPTD']) # QPPGEmessage handler
def send_QPTD(message):
    bot.reply_to(message, (' TRANSMISSION AND DISTRIBUTION MODEL PAPERS '))
    bot.reply_to(message, ('MODEL PAPER 1\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee43-transmission-distribution-model-question-paper-1.pdf'))
    bot.reply_to(message, ('MODEL PAPER 2\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee43-transmission-distribution-model-question-paper-2.pdf'))
@bot.message_handler(commands=['NotesTD']) # notes message handler
def send_NotesTD(message):
    bot.reply_to(message, ('/TD_module1\n' '/TD_module2\n' '/TD_module3\n' '/TD_module4\n' '/TD_module5\n'))
@bot.message_handler(commands=['PGE_module1'])# module1 message handler
def send_TDmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TD_module2'])# module2 message handler
def send_TDmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TD_module3'])# module3 message handler
def send_TDmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TD_module4'])# module4 message handler
def send_TDmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['TD_module5'])# module5 message handler
def send_TDmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..................................................................................................................

@bot.message_handler(commands=['18EE44_EM']) # 18EE44_EM message handler
def send_3th_semEM (message):
    bot.reply_to(message, (' ELECTRIC MOTORS '))
    bot.reply_to(message, ('/QPEM  For question papers\n' '/NotesEM For module wise Notes\n '))
@bot.message_handler(commands=['QPEM']) # QPPGEmessage handler
def send_QPEM (message):
    bot.reply_to(message, (' ELECTRIC MOTORS MODEL PAPERS '))
    bot.reply_to(message, ('MODEL PAPER 1\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee44-electric-motors-model-question-paper-1.pdf'))
    bot.reply_to(message, ('MODEL PAPER 2\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee44-electric-motors-model-question-paper-2.pdf'))
@bot.message_handler(commands=['NotesEM ']) # notes message handler
def send_NotesEM (message):
    bot.reply_to(message, ('/EM_module1\n' '/EM_module2\n' '/EM_module3\n' '/EM_module4\n' '/EM_module5\n'))
@bot.message_handler(commands=['EM _module1'])# module1 message handler
def send_EMmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EM_module2'])# module2 message handler
def send_EMmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EM_module3'])# module3 message handler
def send_EMmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EM_module4'])# module4 message handler
def send_EMmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EM_module5'])# module5 message handler
def send_EMmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#...................................................................................................................

@bot.message_handler(commands=['18EE45_EFT']) # 18EE45_EFT message handler
def send_3th_semEFT (message):
    bot.reply_to(message, (' ELECTROMAGNETIC FIELD THEORY  '))
    bot.reply_to(message, ('/QPEFT  For question papers\n' '/NotesEFT For module wise Notes\n '))
@bot.message_handler(commands=['QPEFT']) # QPPGEmessage handler
def send_QPEFT (message):
    bot.reply_to(message, (' ELECTROMAGNETIC FIELD THEORY MODEL PAPERS '))
    bot.reply_to(message, ('MODEL PAPER 1\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee45-electromagnetic-field-theory-model-question-paper-1.pdf'))
    bot.reply_to(message, ('MODEL PAPER 2\n'' https://www.vturesource.com/vtu-model-question-papers-2017/18ee45-electromagnetic-field-theory-model-question-paper-2.pdf '))
@bot.message_handler(commands=['NotesEFT']) # notes message handler
def send_NotesEFT (message):
    bot.reply_to(message, ('/EFT_module1\n' '/EFT_module2\n' '/EFT_module3\n' '/EFT_module4\n' '/EFT_module5\n'))
@bot.message_handler(commands=['EFT _module1'])# module1 message handler
def send_EFTmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EFT_module2'])# module2 message handler
def send_EFTmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EFT_module3'])# module3 message handler
def send_EFTmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EFT_module4'])# module4 message handler
def send_EFTmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EFT_module5'])# module5 message handler
def send_EFTmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))


#....................................................................................................................

@bot.message_handler(commands=['18EE46_OLIC']) # 18EE46_OLIC message handler
def send_3th_semOLIC (message):
    bot.reply_to(message, (' OPERATIONAL AMPLIFIERS AND LINEAR ICs  '))
    bot.reply_to(message, ('/QPOLIC  For question papers\n' '/NotesOLIC For module wise Notes\n '))
@bot.message_handler(commands=['QPOLIC']) # QPPGEmessage handler
def send_QPOLIC (message):
    bot.reply_to(message, (' OPERATIONAL AMPLIFIERS AND LINEAR ICs MODEL PAPERS '))
    bot.reply_to(message, ('MODEL PAPER 1\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee46-OPERATIONAL-AMPLIFIERS-LINEAR-ICs-model-question-paper-1.pdf'))
    bot.reply_to(message, ('MODEL PAPER 2\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee46-OPERATIONAL-AMPLIFIERS-LINEAR-ICs-model-question-paper-2.pdf'))
    bot.reply_to(message, ('MODEL PAPER 2\n''https://www.vturesource.com/vtu-model-question-papers-2017/18ee46-OPERATIONAL-AMPLIFIERS-LINEAR-ICs-model-question-paper-3.pdf'))
@bot.message_handler(commands=['NotesOLIC']) # notes message handler
def send_NotesOLIC (message):
    bot.reply_to(message, ('/OLIC_module1\n' '/OLIC_module2\n' '/OLIC_module3\n' '/OLIC_module4\n' '/OLIC_module5\n'))
@bot.message_handler(commands=['OLIC _module1'])# module1 message handler
def send_OLICmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OLIC_module2'])# module2 message handler
def send_OLICmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OLIC_module3'])# module3 message handler
def send_OLICmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OLIC_module4'])# module4 message handler
def send_OLICmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OLIC_module5'])# module5 message handler
def send_OLICmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
#.....................................................................................................................





#.................... 5th SEM data handing part................................................. 
@bot.message_handler(commands=['5th_sem']) # 5th sem message handler
def send_5th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 5th sem. '))
    bot.reply_to(message, ('Select the subjects.. '))
    bot.reply_to(message, ('/18EE51_MEN\n''/18EE52_MC\n' '/18EE53_PE\n' '/18EE54_SS\n' '/18EE55_EMD\n' '/18EE56_HVE\n'))

#...............................................................................................................................

@bot.message_handler(commands=['18EE51_MEN']) # 18EE51_MEN message handler
def send_3th_semMEN(message):
    bot.reply_to(message, ('MANAGEMENT AND ENTREPRENEURSHIP '))
    bot.reply_to(message, ('/QP_MEN For question papers\n' '/NotesMEN For module wise Notes\n '))
@bot.message_handler(commands=['QP_MEN']) # QPMEN message handler
def send_QPMEN(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesMEN']) # notes message handler
def send_NotesMEN(message):
    bot.reply_to(message, ('/MEN_module1\n' '/MEN_module2\n' '/MEN_module3\n' '/MEN_module4\n' '/MEN_module5\n'))
@bot.message_handler(commands=['MEN_module1'])# module1 message handler
def send_MENmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MEN_module2'])# module2 message handler
def send_MENmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MEN_module3'])# module3 message handler
def send_MENmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MEN_module4'])# module4 message handler
def send_MENmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MEN_module5'])# module5 message handler
def send_MENmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#.................................................................................................................................

@bot.message_handler(commands=['18EE52_MC']) # 18EE52_MC message handler
def send_3th_semMC(message):
    bot.reply_to(message, (' MICROCONTROLLER '))
    bot.reply_to(message, ('/QP_MC For question papers\n' '/NotesMC For module wise Notes\n '))
@bot.message_handler(commands=['QP_MC']) # QPMC message handler
def send_QPMC(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesMC']) # notes message handler
def send_NotesMC(message):
    bot.reply_to(message, ('/MC_module1\n' '/MC_module2\n' '/MC_module3\n' '/MC_module4\n' '/MC_module5\n'))
@bot.message_handler(commands=['MC_module1'])# module1 message handler
def send_MCmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MC_module2'])# module2 message handler
def send_MCmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MC_module3'])# module3 message handler
def send_MCmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MC_module4'])# module4 message handler
def send_MCmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['MC_module5'])# module5 message handler
def send_MCmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..........................................................................................................................

@bot.message_handler(commands=['18EE53_PE']) # 18EE53_PE message handler
def send_3th_semPE(message):
    bot.reply_to(message, (' POWER ELECTRONICS'))
    bot.reply_to(message, ('/QP_PE For question papers\n' '/NotesPE For module wise Notes\n '))
@bot.message_handler(commands=['QP_MC']) # QPMC message handler
def send_QPPE(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesPE']) # notes message handler
def send_NotesPE(message):
    bot.reply_to(message, ('/PE_module1\n' '/PE_module2\n' '/PE_module3\n' '/PE_module4\n' '/PE_module5\n'))
@bot.message_handler(commands=['PE_module1'])# module1 message handler
def send_PEmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PE_module2'])# module2 message handler
def send_PEmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PE_module3'])# module3 message handler
def send_PEmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PE_module4'])# module4 message handler
def send_PEmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PE_module5'])# module5 message handler
def send_PEmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#......................................................................................................................

@bot.message_handler(commands=['18EE54_SS']) # 18EE54_SS message handler
def send_3th_semSS(message):
    bot.reply_to(message, (' SIGNALS AND SYSTEMS '))
    bot.reply_to(message, ('/QP_SS For question papers\n' '/NotesSS For module wise Notes\n '))
@bot.message_handler(commands=['QP_SS']) # QPMC message handler
def send_QPSS(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesSS']) # notes message handler
def send_NotesSS(message):
    bot.reply_to(message, ('/SS_module1\n' '/SS_module2\n' '/SS_module3\n' '/SS_module4\n' '/SS_module5\n'))
@bot.message_handler(commands=['SS_module1'])# module1 message handler
def send_SSmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['SS_module2'])# module2 message handler
def send_SSmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['SS_module3'])# module3 message handler
def send_SSmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['SS_module4'])# module4 message handler
def send_SSmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['SS_module5'])# module5 message handler
def send_SSmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#.......................................................................................................................

@bot.message_handler(commands=['18EE55_EMD']) # 18EE55_EMD message handler
def send_3th_semEMD(message):
    bot.reply_to(message, (' ELECTRICAL MACHINE DESIGN '))
    bot.reply_to(message, ('/QP_EMD For question papers\n' '/NotesEMD For module wise Notes\n '))
@bot.message_handler(commands=['QP_EMD']) # QPMC message handler
def send_QPEMD(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesEMD']) # notes message handler
def send_NotesEMD(message):
    bot.reply_to(message, ('/EMD_module1\n' '/EMD_module2\n' '/EMD_module3\n' '/EMD_module4\n' '/EMD_module5\n'))
@bot.message_handler(commands=['EMD_module1'])# module1 message handler
def send_EMDmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EMD_module2'])# module2 message handler
def send_EMDmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EMD_module3'])# module3 message handler
def send_EMDmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EMD_module4'])# module4 message handler
def send_EMDmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EMD_module5'])# module5 message handler
def send_EMDmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#.......................................................................................................................

@bot.message_handler(commands=['18EE56_HVE']) # 18EE56_HVE message handler
def send_3th_semHVE(message):
    bot.reply_to(message, (' HIGH VOLTAGE ENGINEERING '))
    bot.reply_to(message, ('/QP_HVE For question papers\n' '/NotesHVE For module wise Notes\n '))
@bot.message_handler(commands=['QP_HVE']) # QPMC message handler
def send_QPHVE(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesHVE']) # notes message handler
def send_NotesHVE(message):
    bot.reply_to(message, ('/HVE_module1\n' '/HVE_module2\n' '/HVE_module3\n' '/HVE_module4\n' '/HVE_module5\n'))
@bot.message_handler(commands=['HVE_module1'])# module1 message handler
def send_HVEmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['HVE_module2'])# module2 message handler
def send_HVEmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['HVE_module3'])# module3 message handler
def send_HVEmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['HVE_module4'])# module4 message handler
def send_HVEmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['HVE_module5'])# module5 message handler
def send_HVEmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#.......................................................................................................................





#.................... 6th SEM data handing part................................................. 
@bot.message_handler(commands=['6th_sem']) # 6th sem message handler
def send_6th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 6th sem. '))
    bot.reply_to(message, ('Select the subjects.. '))
    bot.reply_to(message, ('/18EE61_CS\n''/18EE62_PSA\n' '/18EE63_DSP\n' '/18EE641_INP\n' '/18EE642_EEM\n' '/18EE643_CAED\n' '/18EE644_ES\n' '/18EE64_OPPC++\n'))
#................................................................................................................................

@bot.message_handler(commands=['18EE61_CS']) # 18EE61_CS message handler
def send_6th_semCS(message):
    bot.reply_to(message, (' CONTROLL SYSTEMS '))
    bot.reply_to(message, ('/QP_CS For question papers\n' '/NotesCS For module wise Notes\n '))
@bot.message_handler(commands=['QP_CS']) # QPCS message handler
def send_QPCS(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesCS']) # notes message handler
def send_NotesCS(message):
    bot.reply_to(message, ('/CS_module1\n' '/CS_module2\n' '/CS_module3\n' '/CS_module4\n' '/CS_module5\n'))
@bot.message_handler(commands=['CS_module1'])# module1 message handler
def send_CSmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CS_module2'])# module2 message handler
def send_CSmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CS_module3'])# module3 message handler
def send_CSmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CS_module4'])# module4 message handler
def send_CSmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CS_module5'])# module5 message handler
def send_CSmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#...........................................................................................................

@bot.message_handler(commands=['18EE62_PSA']) # 18EE62_PSA message handler
def send_6th_semPSA(message):
    bot.reply_to(message, (' POWER SYSTEM ANALYSIS – 1 '))
    bot.reply_to(message, ('/QP_PSA For question papers\n' '/NotesPSA For module wise Notes\n '))
@bot.message_handler(commands=['QP_PSA']) # QPCS message handler
def send_QPPSA(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesPSA']) # notes message handler
def send_NotesPSA(message):
    bot.reply_to(message, ('/PSA_module1\n' '/PSA_module2\n' '/PSA_module3\n' '/PSA_module4\n' '/PSA_module5\n'))
@bot.message_handler(commands=['PSA_module1'])# module1 message handler
def send_PSAmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSA_module2'])# module2 message handler
def send_PSAmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSA_module3'])# module3 message handler
def send_PSAmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSA_module4'])# module4 message handler
def send_PSAmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSA_module5'])# module5 message handler
def send_PSAmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))


#..........................................................................................................

@bot.message_handler(commands=['18EE63_DSP']) # 18EE62_DSP message handler
def send_6th_semDSP(message):
    bot.reply_to(message, (' DIGITAL SIGNAL PROCESSING '))
    bot.reply_to(message, ('/QP_DSP For question papers\n' '/NotesDSP For module wise Notes\n '))
@bot.message_handler(commands=['QP_DSP']) # QPCS message handler
def send_QPDSP(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesDSP']) # notes message handler
def send_NotesDSP(message):
    bot.reply_to(message, ('/DSP_module1\n' '/DSP_module2\n' '/DSP_module3\n' '/DSP_module4\n' '/DSP_module5\n'))
@bot.message_handler(commands=['DSP_module1'])# module1 message handler
def send_DSPmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSP_module2'])# module2 message handler
def send_DSPmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSP_module3'])# module3 message handler
def send_DSPmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSP_module4'])# module4 message handler
def send_DSPmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['DSP_module5'])# module5 message handler
def send_DSPmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#...........................................................................................................

@bot.message_handler(commands=['18EE641_INP']) # 18EE641_INP message handler
def send_6th_semINP(message):
    bot.reply_to(message, (' INTRODUCTION TO NUCLEAR POWER  '))
    bot.reply_to(message, ('/QP_INP For question papers\n' '/NotesINP For module wise Notes\n '))
@bot.message_handler(commands=['QP_DSP']) # QPCS message handler
def send_QPINP(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesINP']) # notes message handler
def send_NotesINP(message):
    bot.reply_to(message, ('/INP_module1\n' '/INP_module2\n' '/INP_module3\n' '/INP_module4\n' '/INP_module5\n'))
@bot.message_handler(commands=['INP_module1'])# module1 message handler
def send_INPmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['INP_module2'])# module2 message handler
def send_INPmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['INP_module3'])# module3 message handler
def send_INPmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['INP_module4'])# module4 message handler
def send_INPmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['INP_module5'])# module5 message handler
def send_INPmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..........................................................................................................

@bot.message_handler(commands=['18EE642_EEM']) # 18EE642_EEM message handler
def send_6th_semEEM1(message):
    bot.reply_to(message, (' ELECTRICAL ENGINEERING MATERIALS  '))
    bot.reply_to(message, ('/QP_EEM For question papers\n' '/NotesEEM For module wise Notes\n '))
@bot.message_handler(commands=['QP_EEM']) # QPCS message handler
def send_QPEEM1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesEEM']) # notes message handler
def send_NotesEEM1(message):
    bot.reply_to(message, ('/EEM_module1\n' '/EEM_module2\n' '/EEM_module3\n' '/EEM_module4\n' '/EEM_module5\n'))
@bot.message_handler(commands=['EEM_module1'])# module1 message handler
def send_EEM1module1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module2'])# module2 message handler
def send_EEM1module2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module3'])# module3 message handler
def send_EEM1module3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module4'])# module4 message handler
def send_EEM1module4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEM_module5'])# module5 message handler
def send_EEM1module5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..........................................................................................................

@bot.message_handler(commands=['18EE643_CAED']) # 18EE642_EEM message handler
def send_6th_semCAED(message):
    bot.reply_to(message, (' ELECTRICAL ENGINEERING MATERIALS  '))
    bot.reply_to(message, ('/QP_CAED For question papers\n' '/NotesCAED For module wise Notes\n '))
@bot.message_handler(commands=['QP_CAED']) # QPCS message handler
def send_QPCAED(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesCAED']) # notes message handler
def send_NotesCAED(message):
    bot.reply_to(message, ('/CAED_module1\n' '/CAED_module2\n' '/CAED_module3\n' '/CAED_module4\n' '/CAED_module5\n'))
@bot.message_handler(commands=['CAED_module1'])# module1 message handler
def send_CAEDmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CAED_module2'])# module2 message handler
def send_CAEDmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CAED_module3'])# module3 message handler
def send_CAEDmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CAED_module4'])# module4 message handler
def send_CAEDmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['CAED_module5'])# module5 message handler
def send_CAEDmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..........................................................................................................

@bot.message_handler(commands=['18EE644_ES']) # 18EE644_ES message handler
def send_6th_semES(message):
    bot.reply_to(message, (' EMBEDDED SYSTEMS  '))
    bot.reply_to(message, ('/QP_ES For question papers\n' '/NotesES For module wise Notes\n '))
@bot.message_handler(commands=['QP_ES']) # QPCS message handler
def send_QPES(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesES']) # notes message handler
def send_NotesES(message):
    bot.reply_to(message, ('/ES_module1\n' '/ES_module2\n' '/ES_module3\n' '/ES_module4\n' '/ES_module5\n'))
@bot.message_handler(commands=['ES_module1'])# module1 message handler
def send_ESmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ES_module2'])# module2 message handler
def send_ESmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ES_module3'])# module3 message handler
def send_ESmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ES_module4'])# module4 message handler
def send_ESmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['ES_module5'])# module5 message handler
def send_ESmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..........................................................................................................

@bot.message_handler(commands=['18EE64_OPPC']) # 18EE64_OPPC message handler
def send_6th_semOPPC(message):
    bot.reply_to(message, (' OBJECT ORIENTED PROGRAMMING USING C++ '))
    bot.reply_to(message, ('/QP_OPPC For question papers\n' '/NotesOPPC For module wise Notes\n '))
@bot.message_handler(commands=['QP_OPPC']) # QPCS message handler
def send_QPOPPC(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesOPPC']) # notes message handler
def send_NotesOPPC(message):
    bot.reply_to(message, ('/OPPC_module1\n' '/OPPC_module2\n' '/OPPC_module3\n' '/OPPC_module4\n' '/OPPC_module5\n'))
@bot.message_handler(commands=['OPPC_module1'])# module1 message handler
def send_OPPCmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OPPC_module2'])# module2 message handler
def send_OPPCmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OPPC_module3'])# module3 message handler
def send_OPPCmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OPPC_module4'])# module4 message handler
def send_OPPCmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['OPPC_module5'])# module5 message handler
def send_OPPCmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#..........................................................................................................






#.................... 7th SEM data handing part............................................................................................ 
@bot.message_handler(commands=['7th_sem']) # 6th sem message handler
def send_7th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 7th sem. '))
    bot.reply_to(message, ('Select the subjects.. '))
    bot.reply_to(message, ('/18EE71_PSA2\n''/18EE72_PSP\n' '/18EE731_SWE\n' '/18EE732_ST\n' '/18EE733_IDG\n' '/18EE734_ACS\n' '/18EE735_CEPS\n' 
                            '/18EE741_IDA\n' '/18EE742_UEP\n' '/18EE743_PLCS\n' '/18EE744_SG\n' '/18EE745_ANNPS\n'))
#.............................................................................................................................................



#...........................................................................................................

#.................... 8th SEM data handing part................................................. 
@bot.message_handler(commands=['8th_sem']) # 6th sem message handler
def send_8th_sem(message):
    bot.reply_to(message, ('Here you will find the best Details notes for 8th sem. '))
    bot.reply_to(message, ('Select the subjects.. '))
    bot.reply_to(message, ('/18EE81_PSOC\n''/18EE821_FHVDC\n' '/18EE822_EEC\n' '/18EE823_EVT\n' '/18EE824_PSP\n' '/18EE825_EPQ\n' ))
#........................................................................................

@bot.message_handler(commands=['18EE81_PSOC']) # 18EE64_OPPC message handler
def send_8th_semPSOC(message):
    bot.reply_to(message, (' POWER SYSTEM OPERATION AND CONTROL '))
    bot.reply_to(message, ('/QP_PSOC For question papers\n' '/NotesPSOC For module wise Notes\n '))
@bot.message_handler(commands=['QP_PSOC']) # QPCS message handler
def send_QPPSOC(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesPSOC']) # notes message handler
def send_NotesPSOC(message):
    bot.reply_to(message, ('/PSOC_module1\n' '/PSOC_module2\n' '/PSOC_module3\n' '/PSOC_module4\n' '/PSOC_module5\n'))
@bot.message_handler(commands=['PSOC_module1'])# module1 message handler
def send_PSOCmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSOC_module2'])# module2 message handler
def send_PSOCmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSOC_module3'])# module3 message handler
def send_PSOCmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSOC_module4'])# module4 message handler
def send_PSOCmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['PSOC_module5'])# module5 message handler
def send_PSOCmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#........................................................................................

@bot.message_handler(commands=['18EE821_FHVDC']) # 18EE821_FHVDC message handler
def send_8th_semFHVDC(message):
    bot.reply_to(message, ('FACTS AND HVDC TRANSMISSION  '))
    bot.reply_to(message, ('/QP_FHVDC For question papers\n' '/NotesFHVDC For module wise Notes\n '))
@bot.message_handler(commands=['QP_FHVDC']) # QPCS message handler
def send_QPFHVDC(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesFHVDC']) # notes message handler
def send_NotesFHVDC(message):
    bot.reply_to(message, ('/FHVDC_module1\n' '/FHVDC_module2\n' '/FHVDC_module3\n' '/FHVDC_module4\n' '/FHVDC_module5\n'))
@bot.message_handler(commands=['FHVDC_module1'])# module1 message handler
def send_FHVDCmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['FHVDC_module2'])# module2 message handler
def send_FHVDCmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['FHVDC_module3'])# module3 message handler
def send_FHVDCmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['FHVDC_module4'])# module4 message handler
def send_FHVDCmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['FHVDC_module5'])# module5 message handler
def send_FHVDCmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#........................................................................................
 
@bot.message_handler(commands=['18EE822_EEC']) # 18EE822_EEC message handler
def send_8th_semEEC(message):
    bot.reply_to(message, ('FACTS AND HVDC TRANSMISSION  '))
    bot.reply_to(message, ('/QP_EEC For question papers\n' '/NotesEEC For module wise Notes\n '))
@bot.message_handler(commands=['QP_EEC']) # QPCS message handler
def send_QPEEC(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you question paper'))
@bot.message_handler(commands=['NotesEEC']) # notes message handler
def send_NotesEEC(message):
    bot.reply_to(message, ('/EEC_module1\n' '/EEC_module2\n' '/EEC_module3\n' '/FHVDC_module4\n' '/FHVDC_module5\n'))
@bot.message_handler(commands=['EEC_module1'])# module1 message handler
def send_EECmodule1(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEC_module2'])# module2 message handler
def send_EECmodule2(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEC_module3'])# module3 message handler
def send_EECmodule3(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEC_module4'])# module4 message handler
def send_EECmodule4(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))
@bot.message_handler(commands=['EEC_module5'])# module5 message handler
def send_EECmodule5(message):
    bot.reply_to(message, ('Hey! buddy am under testing.. I will be upadating to get you notes'))

#........................................................................................


#...................... DONT TOUCH.............................................................................
while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)

