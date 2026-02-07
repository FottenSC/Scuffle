import requests
from multiprocessing import queues #pyinstaller workaround  https://stackoverflow.com/questions/40768570/importerror-no-module-named-queue-while-running-my-app-freezed-with-cx-freeze
import json

CURRENT_VERSION = 'scuffle_VV_2.2'

def check_version(force_print=False):

    new_version_available = False
    if 'dev' in CURRENT_VERSION:
        print("SCUFFLE version check disabled.")
        print("DEVELOPER NOTE: Remember to update VersionChecker.CURRENT_VERSION before publishing a release.")
    else:
        try:
            r = requests.get('https://api.github.com/repositories/437065963/releases')

            #https://api.github.com
            #GET /repos/:owner/:repo/releases/latest
            if r.ok:
                available_updates = 0
                repoItem = json.loads(r.text or r.content)
                for release in repoItem:
                    if release['tag_name'] != CURRENT_VERSION:
                        if CURRENT_VERSION.split('scuffle_VV_')[1] > str(release['tag_name']).split('scuffle_VV_')[1]:
                            break
                        available_updates += 1
                    else:
                        break
                
                if (available_updates > 0):
                    print("---------------------------------------------------------" * 2)
                    print("** A new version of SCUFFLE is available. **")
                    print("")
                    #if (repoTag != CURRENT_VERSION or force_print):
                    #print(repoItem['html_url'])
                    print("Release Notes:")
                    new_version_available = True
                    while available_updates > 0:
                        index = available_updates - 1
                        repoTag = str(repoItem[index]['tag_name'])
                        print(f"{repoTag.split('scuffle_VV_')[1]}:")
                        print(repoItem[index]['body'])
                        available_updates -= 1
                    print("---------------------------------------------------------" * 2)
                else:
                    print("SCUFFLE is up to date.")
            else:
                print("Unable to contact github repo")
        except:
            print("SCUFFLE version check failed (no internet?).")
    print("")
    return new_version_available


if __name__ == '__main__':
    check_version()