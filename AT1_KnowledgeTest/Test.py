# import random number generator module
import random

# set min and max values
min_value = 1
max_value = 50

# Generate a random whole number between 1-50
secret_number = random.randint(min_value, max_value)

# set the default value for guess to Zero
user_guess = 0

# set attempts value
attempts = 0

print(secret_number)

nix repl -f '<nixpkgs>'
Nix 2.34.0
Type :? for help.
Loading installable ''...
Added 26495 variables.
AAAAAASomeThingsFailToEvaluate, AMB-plugins, ArchiSteamFarm, AusweisApp2, CHOWTapeModel, ChowCentaur, ChowKick, ChowPhaser, CoinMP, CuboCore, DisnixWebService, EBTKS, EmptyEpsilon, FIL-plugins, Fabric, HentaiAtHome, LAStools, LASzip, LASzip2, LPCNet
... and 26475 more; view with :ll
nix-repl> :b   (python3.withPackages (python-pkgs: with python-pkgs; [
      dateutils
      icalendar
      ical
      markdown
      soupsieve #BeautifulSoup, converts html to txt
      beautifulsoup4
        >       dateutils
        >       icalendar
        >       ical
        >       markdown
        >       soupsieve #BeautifulSoup, converts html to txt
        >       beautifulsoup4
        >   ]))

This derivation produced the following outputs:
  out -> /nix/store/mx307b575sj0w7cy95d1f3a2fwqgnbvs-python3-3.13.12-env


❯ /nix/store/mx307b575sj0w7cy95d1f3a2fwqgnbvs-python3-3.13.12-env/bin/python
Python 3.13.12 (main, Feb  3 2026, 17:53:27) [Clang 21.1.8 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import markdown
>>> markdown.
markdown.Extension(         markdown.blockparser        markdown.extensions         markdown.markdown(          markdown.preprocessors      markdown.util
markdown.Markdown(          markdown.blockprocessors    markdown.htmlparser         markdown.markdownFromFile(  markdown.serializers
markdown.annotations        markdown.core               markdown.inlinepatterns     markdown.postprocessors     markdown.treeprocessors