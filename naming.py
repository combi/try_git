import sys
import re

'''
    lsFilter = '%s%s_*_%s' %(ns,basename,suffix)
    reFilter = r'%s%s_(\d+)_%s' %(ns,basename,suffix)
'''


def clearScreen():
    print '\n'*50

def getNumeratedNameSimple(nameInput, keepNs=True, sceneNames=[]):

    nameOutput = ''
    nodeName = nameInput
    # --------------------------------------------------------------------------
    # -- We separate namespace and real objName
    #
    nsPattern = r'(:?[\w:]*:)?(\w+)'
    m         = re.search(nsPattern, nameInput)
    ns        = m.group(1) or '' # group(0) is the full match ungrouped
    nameNoNs  = m.group(2)

    ns = re.sub('^:','',ns) # just in case we have a name with root namespace passed in

    print 'nameInput => %s (keepNs %s)' %(nameInput, keepNs)
    print '  - ns        = ', ns
    print '  - nameNoNs  = ', nameNoNs

    if not keepNs:
        ns        = ''
        nameInput = nameNoNs

    # nodeName will be used to do a first scene search for a node with nameInput
    print 'used name = ', nameInput

    # --------------------------------------------------------------------------
    # -- If nodeName is absent from scene we can use it directly
    #
    # if not nameInput in cmds.ls(nameInput):
    if not nameInput in sceneNames:
        nameOutput = nameInput
        print'nameOutput =',nameOutput
        return nameOutput

    # --------------------------------------------------------------------------
    # -- If nodeName is found in scene we need to find other numerated names
    # -- If nodeName has a syntax, numerated names should look like 'any_basename_#_suffix'
    # -- If nodeName has a NO syntax, numerated names should look like 'aShittyName#'
    #
    nameIsSyntaxed = True
    lsFilter       = ''
    reFilter       = ''
    basename       = ''
    num            = ''
    suffix         = ''

    if '_' in nameInput:
        syntaxPattern = r'([\w]+?)(?:(?:_)(\d+))*_(\w+)' # notation r'' means the string is a raw string (does not try to escape any character)
        syntaxScan    = re.search(syntaxPattern, nameInput)
        basename = scan.group(1) or ''
        num      = scan.group(2) or ''
        suffix   = scan.group(3) or ''



    if syntaxScan:
        lsFilter = '%s%s_*_%s' %(ns,basename,suffix)
        reFilter = r'%s%s_(\d+)_%s' %(ns,basename,suffix)
    else:
        lsFilter = '%s%s_*_%s' %(ns,basename,suffix)
        reFilter = r'%s%s_(\d+)_%s' %(ns,basename,suffix)
        nameIsSyntaxed = False



    print ''
    return nameOutput






if __name__ == "__main__":

    clearScreen()

    sceneNames = []
    sceneNames.append('toto')
    sceneNames.append('NS:toto')
    sceneNames.append(':NS:toto')
    sceneNames.append(':NS1:NS2:toto')

    sceneNames.append('toto1')
    sceneNames.append('NS:toto1')
    sceneNames.append(':NS:toto1')
    sceneNames.append(':NS1:NS2:toto1')

    sceneNames.append('toto_obj')
    sceneNames.append('NS:toto_obj')
    sceneNames.append(':NS:toto_obj')
    sceneNames.append(':NS1:NS2:toto_obj')

    sceneNames.append('toto_1_obj')
    sceneNames.append('NS:toto_1_obj')
    sceneNames.append(':NS:toto_1_obj')
    sceneNames.append(':NS1:NS2:toto_1_obj')
    nameToTest = sys.argv[-1]
    result = getNumeratedNameSimple(nameToTest, sceneNames=sceneNames, keepNs=True)
    print '\n'
    result = getNumeratedNameSimple(nameToTest, sceneNames=sceneNames, keepNs=False)
    sys.exit()


'''
name = 'plop_toto_1_suffix'
print len(name)
pattern = re.compile(r'^\w+(?!_\d+_)')
# pattern = re.compile(r'(^\w+)_([a-zA-Z]+$)')
result = pattern.search(name)
print result.start(), result.end()
print result.groups()
'''
'''
pattern = re.compile(r"(\d\d-)?(\w{3,4})-(?(1)(\d\d)|[a-z]{3,4})$")
# pattern = re.compile(r"(?(\d\d)|[a-z]{3,4})$")
m = pattern.search("34-erte-22")
m = pattern.search("34-erte")
m = pattern.search("erte-toto")
print m.groups()

'''
