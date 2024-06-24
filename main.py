import shutil
import discord
import asyncio
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style
import os
from datetime import datetime
import threading
from packaging import version
import requests
import aiohttp

lp = "\033[38;2;0;255;255m"
dp = "\033[38;2;154;77;255m"
w = "\033[1;37m"
red = "\033[1;31m"
dark_gray = "\033[1;90m"
r = Style.RESET_ALL

Usernamefiley = "username.txt"
current_time = datetime.now().strftime("%H:%M:%S")

def load_tokens():
    if os.path.exists('tokens.txt'):
        with open('tokens.txt', 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
            return tokens, len(tokens)
    return [], 0

tokens, num_tokens = load_tokens()

def save_username(username):
    with open(Usernamefiley, "w") as file:
        file.write(username)

def load_username():
    if os.path.exists(Usernamefiley):
        with open(Usernamefiley, "r") as file:
            return file.read().strip()
    return None

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

username = load_username()

async def spam(token, target, message, count):
    try:
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)
        os.system(f'title Spamming {target}')

        @client.event
        async def on_ready():
            await asyncio.sleep(1)
            threading.Thread(target=loginmsg, args=(client.user.name, token)).start()
            await asyncio.sleep(1)

            target_user = await client.fetch_user(int(target))

            for _ in range(count):
                try:
                    await target_user.send(message)
                    await asyncio.sleep(0.5)
                    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {lp}[YES]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Sent message to {target_user.name} | {token[:len(token)//2]}******"))

                except discord.Forbidden:
                    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"{target_user.name} DMs are closed | {token[:len(token)//2]}******"))
                    continue
                except Exception as nigger:
                    print(f"{nigger}")
                    break

            await client.close()

        await client.start(token)

    except discord.NotFound:
        print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Couldnt find user"))
    except discord.LoginFailure:
        print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Invalid Token | {token[:len(token)//2]}******"))
    except Exception as stupid:
        print(f"{stupid}")

def loginmsg(username, token):
    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {lp}[YESS]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Logged in as {username} | {token[:len(token)//2]}******"))

async def embed_spam(token, target, title, description, footer, count):
    try:
        intents = discord.Intents.all()
        client = discord.Client(intents=intents)
        os.system(f'title Spamming {target}')

        @client.event
        async def on_ready():
            await asyncio.sleep(1)
            threading.Thread(target=loginmsg, args=(client.user.name, token)).start()
            await asyncio.sleep(1)

            target_user = await client.fetch_user(int(target))
            embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
            embed.set_footer(text=footer)

            for _ in range(count):
                try:
                    await target_user.send(embed=embed)
                    await asyncio.sleep(0.5)
                    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {dp}[YES!]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Sent embed to {target_user.name} | {token[:len(token)//2]}******"))

                except discord.Forbidden:
                    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"{target_user.name} DMs are closed | {token[:len(token)//2]}******"))
                    continue
                except Exception as e:
                    print(f"{e}")
                    break

            await client.close()

        await client.start(token)

    except discord.NotFound:
        print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Couldn't find user"))
    except discord.LoginFailure:
        print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Invalid Token | {token[:len(token)//2]}******"))
    except Exception as e:
        print(f"{e}")
        
def loginmsg(username, token):
    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {dp}[YES!]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Logged in as {username} | {token[:len(token)//2]}******"))
    
def art(username):
    logo = (Colorate.Horizontal(Colors.cyan_to_blue, Center.XCenter(f'''                                                                                     
                                               █████ ░  █     
                █  ██████████          █  ▓▓█████████  ████    
    ███  █     ██   ██      ███  █    ██  ██   ██  ██  ███▒    
    ██   ██    ██  ███      ██▒░███   ██ ███  ███  ██  ██░     
   ███  ███   ██ ██████▒  ███ █████ ▒█░▒██   ██    ████       
  ░██  █████ ██  ██       ██ ██████ ██ ███  ███    ████       
  ██░ ██ ▓█████ ██       ██▓ ██ ██████░██   ██     ██▒        
  ██  ██  ████ ▓█        ██  ██  ████ ▓█    ██     ██░        
 ▒█  ▓█    ░█  █        ▓█  ██    ▒█  █▒    ██    ▒█░         
 ░   █         ░            █                     ██          
''')))

    print(Center.XCenter(logo))

async def rename_bots(new_name):
    for token in tokens:
        try:
            intents = discord.Intents.all()
            client = discord.Client(intents=intents)

            @client.event
            async def on_ready():
                await client.user.edit(username=new_name)
                print(f"{dark_gray}{current_time}{Style.RESET_ALL} {lp}[YES!]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Renamed bot to {new_name} | {token[:len(token)//2]}******"))
                await client.close()

            await client.start(token)
        except discord.LoginFailure:
            print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Invalid Token | {token[:len(token)//2]}******"))

async def change_bio(new_bio):
    for token in tokens:
        try:
            intents = discord.Intents.all()
            client = discord.Client(intents=intents)

            @client.event
            async def on_ready():
                await client.user.edit(bio=new_bio)
                print(f"{dark_gray}{current_time}{Style.RESET_ALL} {lp}[YES!]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Changed bio to {new_bio} | {token[:len(token)//2]}******"))
                await client.close()

            await client.start(token)
        except discord.LoginFailure:
            print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Invalid Token | {token[:len(token)//2]}******"))

async def change_pfp(pfp_url):
    response = requests.get(pfp_url)
    if response.status_code == 200:
        pfp = response.content
        for token in tokens:
            try:
                intents = discord.Intents.all()
                client = discord.Client(intents=intents)

                @client.event
                async def on_ready():
                    await client.user.edit(avatar=pfp)
                    print(f"{dark_gray}{current_time}{Style.RESET_ALL} {lp}[YES!]{Style.RESET_ALL}", Colorate.Horizontal(Colors.green_to_white, f"Changed profile picture | {token[:len(token)//2]}******"))
                    await client.close()

                await client.start(token)
            except discord.LoginFailure:
                print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Invalid Token | {token[:len(token)//2]}******"))
    else:
        print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Failed to fetch image from URL"))

async def send_webhook_invite(webhook_url):
    async with aiohttp.ClientSession() as session:
        for token in tokens:
            try:
                intents = discord.Intents.all()
                client = discord.Client(intents=intents)

                @client.event
                async def on_ready():
                    invite_link = f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
                    await client.close()
                    async with session.post(webhook_url, json={'content': invite_link}) as response:
                        if response.status == 204:
                            print(f"{dark_gray}{current_time}{Style.RESET_ALL} [YES!]", Colorate.Horizontal(Colors.green_to_white, f"Sent invite link to webhook | {token[:len(token)//2]}******"))
                        else:
                            print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Failed to send webhook | {token[:len(token)//2]}******"))

                await client.start(token)
            except discord.LoginFailure:
                print(f"{dark_gray}{current_time}{Style.RESET_ALL} {red}[FAILED]{Style.RESET_ALL}", Colorate.Horizontal(Colors.red_to_white, f"Invalid Token | {token[:len(token)//2]}******"))

async def clear_and_restart():
    clear_console()
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(art)))
    await main()

async def main():
    os.system(f'cls')
    os.system(f'mode 85,20 & title Infinity Spammer Made by Depic')

    global username

    if not username:
        clear_console()
        username = input(f"{lp}username: {Style.RESET_ALL} ")
        save_username(username)

    clear_console()
    art(username)
    print(f"""                    
       {lp}[{w}1{r}{lp}]{r} {w}DM Spam{r}        {lp}[{w}2{r}{lp}]{r} {w}Send Webhook Invite{r}  {lp}[{w}3{r}{lp}]{r} {w}Rename Bots{r}                                      
       {lp}[{w}4{r}{lp}]{r} {w}Change pfp{r}     {lp}[{w}5{r}{lp}]{r} {w}Change Bio{r}           {lp}[{w}6{r}{lp}]{r} {w}Embed DM Spam{r}         """)
    print(Colorate.Horizontal(Colors.cyan_to_blue, f"""
                                Tool Made By Depic
                        https://discord.gg/infinityservices
    """))

    option = input(f"{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, f'┌──<{username}@Infinity')}\n{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, '└──➧ ')}{Style.RESET_ALL}")
    target = None  
    if option == "1":
        target = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'User Id : ')}")
        message = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Message  : ')}")
        message_amount = int(input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Amount per bot : ')}"))
        caca = spam

    elif option == "2":
        webhook_url = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Webhook URL : ')}")
        await send_webhook_invite(webhook_url)

    elif option == "3":
        new_name = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'New Name : ')}")
        await rename_bots(new_name)

    elif option == "4":
        pfp_url = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Profile Picture URL : ')}")
        await change_pfp(pfp_url)

    elif option == "5":
        new_bio = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'New Bio : ')}")
        await change_bio(new_bio)

    elif option == "6":
        target = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'User Id : ')}")
        title = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Embed Title : ')}")
        description = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Embed Description : ')}")
        footer = input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Embed Footer : ')}")
        count = int(input(f"{lp}[CONFIG]{Style.RESET_ALL} {Colorate.Horizontal(Colors.cyan_to_blue, 'Message Amount: ')}"))
        pupu = embed_spam

    elif option == "7":
        print(f"{lp}Exiting...{Style.RESET_ALL}")
        exit()

    else:
        print(f"{red}Invalid option!{Style.RESET_ALL}")
        await clear_and_restart()

    tasks = [caca(token, target, message, message_amount) for token in tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    clear_console()
    asyncio.run(main())
