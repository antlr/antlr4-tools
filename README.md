# antlr4-tools
Tools to run antlr4 w/o needing to install java or antlr4!

## Install

```bash
$ pip install antlr4-tools
```

That creates `antlr4` and `antlr4-parse` executables.

Requires ANTLR 4.10.2 and above for `antlr4-parse` but any version for `antlr4` command.  (Use `antlr-parse -v 4.10.2-SNAPSHOT ...` until 4.10.2 is released.)

Save [this jar](https://oss.sonatype.org/content/repositories/snapshots/org/antlr/antlr4/4.10.2-SNAPSHOT/antlr4-4.10.2-20220530.193833-1-complete.jar) to this dir:

```
/Users/parrt/.m2/repository/org/antlr/antlr4/4.10.2-SNAPSHOT/
```

## Running ANTLR tool on grammars

```bash
$ antlr4
ANTLR Parser Generator  Version 4.10.1
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
```

```bash
$ antlr4 -v 4.9.3
ANTLR Parser Generator  Version 4.9.3
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
```

```bash
$ antlr4 JSON.g4 
$ ls JSON*.java
JSONBaseListener.java  JSONLexer.java         JSONListener.java      JSONParser.java
$ antlr4 -Dlanguage=Python3 -visitor JSON.g4
$ ls JSON*.py
JSONLexer.py     JSONListener.py  JSONParser.py    JSONVisitor.py
```

## Parsing using interpreter

```bash
$ antlr4-parse -v 4.10.2-SNAPSHOT JavaLexer.g4 JavaParser.g4 compilationUnit -profile dump.csv T.java
$ open /tmp/dump.csv 
$ head -5 /tmp/dump.csv 
Rule,Invocations,Time (ms),Total k,Max k,Ambiguities,DFA cache miss
compilationUnit:0,1,0.164791,1,1,0,1
compilationUnit:1,42,1.106583,42,1,0,2
compilationUnit:2,2,1.73675,2,1,0,2
compilationUnit:3,1,3.969,1,1,0,1
```

```bash
$ antlr4-parse -v 4.10.2-SNAPSHOT TParser.g4 TLexer.g4 expr -tokens -trace
abc;
[@0,0:2='abc',<ID>,1:0]
[@1,3:3=';',<';'>,1:3]
[@2,4:4='\n',<WS>,channel=1,1:4]
[@3,5:4='<EOF>',<EOF>,2:0]
enter   expr, LT(1)=abc
enter   a, LT(1)=abc
consume [@0,0:2='abc',<2>,1:0] rule a
consume [@1,3:3=';',<1>,1:3] rule a
exit    a, LT(1)=<EOF>
exit    expr, LT(1)=<EOF>
```
