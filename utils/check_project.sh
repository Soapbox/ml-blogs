#!/bin/bash

#####
##### A script which perform several checks to the entire project.
#####

export IS_UNIT_TEST="True"

linter() {
    echo "###################################################"
    echo "Linter results:"
    echo "###################################################"

    pylint $(find api -iname "*.py" | grep -vi "__init__.py" | grep -vi "config.py") || pylint-exit --error-fail --warn-fail --refactor-fail --convention-fail $?

    if [ $? -ne 0 ]; then
        echo "Linter check failed!"
        echo ""
        exit 1
    fi

    echo "Linter check passed!"
    echo ""
}

unittest() {
    echo "###################################################"
    echo "Unit test results:"
    echo "###################################################"

    for FILENAME in $(find test -iname "*.py")
    do
        echo "###################################################"
        echo "Running tests for $FILENAME"
        echo "###################################################"
        python -m unittest --failfast $FILENAME

        if [ $? -ne 0 ]; then
            echo "Unit test failed!"
            echo ""
            exit 1
        fi
    done
}

if [ "$1" != "--no-linter" ]; then
    linter
fi

unittest

echo ""
echo "Done!"
