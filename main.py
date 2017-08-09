import os.path
import twitter
import time

def main():
    print('    #################################################')
    print('    ############**** -- Simple RT Bot -- ****########')
    print('    ####**** --- By Odin of AlphabetSec --- ****#####')
    print('    #####**** --- Twitter: @0dins_Cr0w --- ****######')
    print('    #################################################')

    username = ''
    password = ''
    hashtag = ''

    print('###########################################################')
    print('#                [Note From Odin]                         #')

    print('# Be Advised: for proper OpSec precautions, no account    #')
    print('# information will be stored on the user\'s computer.      #')
    print('# This may be inconvenient, but it is advised that the    #')
    print('# user does not alter the functionality without properly  #')
    print('# implementing encryption on the stored data. In the case #')
    print('# of compromise, storing passwords in plain text can be   #')
    print('# disastrous...                                           #')
    print('###########################################################')

    while(True):






        apiKey = 'pPHv2LaVczEdFvCZPORnoV7kX'
        SecretKey = 'oaqhIXkmg253oMJLcTQF0RKEW9VBU2yIPi8bSlofYULaFX5bQG'
        if os.path.exists('acctInfo.txt'):
            file = open('acctInfo.txt','r')
            AccToken = file.readline().strip('\n')
            AccTokenSec = file.readline().strip('\n')
            username = file.readline().strip('\n')
            hashtag = file.readline().strip('\n')
            file.close()
        else:
            print('You now will need an access token. For official')
            print('Twitter instructions, visit this link: ')
            print('\nhttps://dev.twitter.com/oauth/overview/application-owner-access-tokens')
            print('Essentially, you need to create a developers account')
            print('in order to give this application access to your')
            print('account. Once you generated the token, copy and paste')
            print('it below.')

            AccToken = input('Access Token: ')
            AccTokenSec = input('Access Token Secret: ')
            file = open('acctInfo.txt','w+')
            file.write(AccToken+'\n'+AccTokenSec+'\n')
            username = input('Username: ')
            file.write(username+'\n')
            hashtag = input('Hashtag: ')
            if '#' not in hashtag:
                hashtag = '#' + hashtag
            file.write(hashtag+'\n')
            file.close()


        api = twitter.Api(consumer_key=apiKey, consumer_secret=SecretKey,
                          access_token_key=AccToken,
                          access_token_secret=AccTokenSec)

        print('Username: ' + username)
        print('Target Hashtag: ' + hashtag)
        while(True):
            try:
                lastMessage = api.GetDirectMessages(count=1,include_entities=True)
            except twitter.error.TwitterError:
                print('[DEBUG] Time Out!')
                time.sleep('60')

            print(lastMessage[0].AsDict()['sender']['screen_name']+' : '+lastMessage[0].AsDict()['text'])
            youGotMail = False
            while(not youGotMail):
                newMessage = api.GetDirectMessages(count=1,include_entities=True)
                if newMessage[0].id != lastMessage[0].id:
                    print('[DEBUG] You got mail!')
                    youGotMail = True
                else:
                    print('[DEBUG] No mail!')
                    time.sleep(60)


            time.sleep(60)





if __name__ == '__main__':
    main()