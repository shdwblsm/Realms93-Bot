def assess(Output,botState,botName):    
    import re 
    from datetime import datetime
    import telnetlib
    from telnetlib import Telnet
    import sys
    
    tn = telnetlib.Telnet("www.windows93.net", 8082)  

        # line = Output
        
    print("You have entered the assess module: " + Output)
    
    #Removing color coding ascii with regex
    colorcodes = r'((\^\[\[\d{1,2}m)(\^M)*)'
    Output = re.sub(colorcodes, '', Output)
    
    print("After Regex: " + Output)
   

    file = open("realms93-regexstrip", "a")
    file.write(Output)
    file.close()
    
    # If multiple lines in buffer, split them
    Output = Output.split('\n')
    # print("After split: " + Output)
    
    
    for line in Output:
            
            print("You have entered the line foreach: " + line)

            if ('Zugzwang whispers to you' in line or 'Bishop whispers to you' in line or 'Argus whispers to you' in line):
            # Accept commands only from whispers from Zugzwang or Bishop/Argus

                print("=========== BOSS WHISPER DETECTED ===========")
                

                # saves line to cmd
                if ('cmd@' in line):
                    
                    
                    cmd = line.split('@')[1]
                    who = line.split(' ')[0]
                    
                    print('WHO: ' + who + ' CMD: ' + cmd)
                          
                    # Save a log
                    now = datetime.now()
                    tstamp = now.strftime("[%m/%d/%Y %H:%M] ")

                    file = open("realms93-cmdlog", "a")
                    file.write(tstamp + who + ': ' + cmd)
                    file.close()

                    if (cmd == "Halt"):
                        # Stop doing anything until "resume" is issued
                        botState = Halt

                        tn.write(b"whisper " + who + " State Change: " + botState.encode('ascii') + b"\n")

                        return botState

                    elif (cmd == "Resume"):
                        # Reset botState to "active"
                        botState = "active"

                        tn.write(b"whisper " + who + " State Change: " + botState.encode('ascii') + b"\n")

                        return botState

                    else:
                        print('Made it to the else statement')
                        # do command
                        
                                               
                        return(cmd)
                        
                        
                        

            elif ('*swings at*' or '*hits*' in line and botName in line):
                # Examples: 
                # Rat swings at Zugzwang but misses!
                # Rat hits Zwischenzug for 1 damage!
                # Rat has died!

                # Get Room State - something for later.
                # roomState = tn.write(b"api").encode(ascii)

                # Check botState and, if not halt, set botState and pull attacker and target from line and save to atk, target variable depending on if it hits or misses
                if (botState == "Halt"):
                    return

                else:
                    botState = "Defending"
                    
                    
                if ('swings at' in line):

                    atk = (line.split(' '))[0]
                    target = (line.split(' '))[3]
                    
                    return(atk, target)

                elif ('hits' in line):

                    atk = (line.split(' '))[0]
                    target = (line.split(' '))[2]                

                    print(atk)
                    print(target)

                    cmd = "a " + atk
                    
                    return(atk, target)

                else:

                    atk = ""
                    target = ""

                    return


                    # Respond to attack -- Use api command for awareness?
                if (target == botName):

                    # Who Attacked Me At a Glance -- possible hitlist for later
                    now = datetime.now()
                    tstamp = now.strftime("[%m/%d/%Y %H:%M] ")
                    file = open("realms93-atk-log", "a")
                    file.write(tstamp + atk)
                    file.close()          

                    interact.attack(atk)

                    return botState

            elif 'drops' in line:

                # Pull $item from line and pass to interact()
                item = line.split(' ')[0]

                # Pick up item
                interact.get(item)

            else:
                print('LINE PROCESSED: ' + line)


    def actions():
        #  Interaction Action cmds


        def look():
            look = "look"

            result = (tn.write(look.encode('ascii') + b"\n"))

            return result

            # cmd Say             
        def say(words):
            (tn.write(words.encode('ascii') + b"\n"))
            result = (tn.write(words.encode('ascii') + b"\n"))

            return result

            # cmd Attack             
        def attack(atk):

            # roomState = tn.write 

            attack = "a atk"

            sleep(1)

            result = (tn.write(atk.encode('ascii') + b"\n"))

            #if result == "You can't attack yet!":
                #    break 

            return result

            # cmd Drop
            # def drop(item)


            # cmd Take             
            # def take(item)

            # cmd Sell
            # def sell(item)    


