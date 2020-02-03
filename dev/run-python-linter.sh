#!/bin/bash

COLOR_FOR_BASH=\\e

if (( $(uname) == 'Darwin' )); then
    COLOR_FOR_BASH=\\x1B
fi

GREEN=$COLOR_FOR_BASH[92m
WHITE=$COLOR_FOR_BASH[39m

if [ -z "$1"  ]; then
    echo -e ${GREEN}Analizing production code...${WHITE}

    pylint adagio_common/ --include-naming-hint=y --variable-rgx='[a-z_][a-z0-9_]{2,50}$' --method-rgx='[A-Za-z_][A-Za-z0-9_]{2,50}' --function-rgx='[A-Za-z_][A-Za-z0-9_]{2,50}' --class-attribute-rgx='([A-Za-z_][A-Za-z0-9_]{2,50}|(__.*__))$'

    echo -e ${GREEN}Analizing test code...${WHITE}

    find adagio_common/*specs/ -name "*.py" | xargs pylint --include-naming-hint=y --variable-rgx='[a-z_][a-z0-9_]{2,50}$' --method-rgx='[A-Za-z_][A-Za-z0-9_]{2,50}' --function-rgx='[A-Za-z_][A-Za-z0-9_]{2,50}' --class-attribute-rgx='([A-Za-z_][A-Za-z0-9_]{2,50}|(__.*__))$'
elif [ $1 = "staged" ]; then
    if [[ $((git status --porcelain | grep '.py$' | grep "M  "; git status --porcelain | grep '.py$' | grep "MM"; git status --porcelain | grep '.py$' | grep "A") | cat | awk '{print $2}') ]]; then
        echo -e ${GREEN}Analizing staged git files...${WHITE}
        (git status --porcelain | grep '.py$' | grep "M  "; git status --porcelain | grep '.py$' | grep "MM"; git status --porcelain | grep '.py$' | grep "A") | cat | awk '{print $2}'| xargs pylint --include-naming-hint=y --variable-rgx='[a-z_][a-z0-9_]{2,50}$' --method-rgx='[A-Za-z_][A-Za-z0-9_]{2,50}' --function-rgx='[A-Za-z_][A-Za-z0-9_]{2,50}' --class-attribute-rgx='([A-Za-z_][A-Za-z0-9_]{2,50}|(__.*__))$'
    else
        echo -e ${GREEN}No found staged git files...${WHITE}
    fi
fi
