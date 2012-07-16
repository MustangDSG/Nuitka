#     Copyright 2012, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Code generation for sets.

Right now only the creation is done here. But more should be added later on.
"""

from .Identifiers import CallIdentifier

from .TupleCodes import getTupleCreationCode

def getSetCreationCode( context, element_identifiers ):
    tuple_identifier = getTupleCreationCode(
        element_identifiers = element_identifiers,
        context             = context
    )

    return CallIdentifier(
        called  = "MAKE_SET",
        args    = ( tuple_identifier.getCodeTemporaryRef(), )
    )
