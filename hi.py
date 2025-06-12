import urllib.parse
import webbrowser
#Archi linux user: afifgodoflinux password:afif2013
def generate_pollinations_link(prompt_path):
    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            prompt = file.read().strip()

        # URL encode the prompt
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://text.pollinations.ai/{encoded_prompt}"

        #print(f"\nGenerated URL:\n{url}\n")
        # Add the url to an txt file
        with open("url.txt", 'w', encoding='utf-8') as fie :
            fie.write(url)
        # Optional: open in default web browser
        

    except FileNotFoundError:
        print(f"[ERROR] File '{prompt_path}' not found.")
    except Exception as e:
        print(f"[EXCEPTION] {e}")

if __name__ == "__main__":
    print("=== Link Generator ===\n")
    prompt_file = input("Enter path to your prompt text file: ")
    generate_pollinations_link(prompt_file)
