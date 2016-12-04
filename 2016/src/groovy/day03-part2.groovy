#!/usr/bin/env groovy

def input = new File('day03.txt') as String[]

int possible = 0

def t = (1..3).collect { [] }
input.each { dims ->
    def dd = dims.split()*.toInteger()
    dd.eachWithIndex { d, i -> t[i] << d }
    if (t.first().size() == 3) {
        possible += t.count {
            def (a, b, c) = it
            println "$a $b $c"
            return (a + b > c && a + c > b && b + c > a)
        }
        t = (1..3).collect { [] }
    }
}

println possible