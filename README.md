# Nano ID

[![CircleCI](https://circleci.com/gh/puyuan/py-nanoid/tree/master.svg?style=svg)](https://circleci.com/gh/puyuan/py-nanoid/tree/master)

A tiny, secure, URL-friendly, unique string ID generator for Python. Original implementation's repository: [https://github.com/ai/nanoid](https://github.com/ai/nanoid).

* __Safe__. It uses cryptographically strong random APIs and tests distribution of symbols.
* __Compact__. It uses a larger alphabet than UUID (A-Za-z0-9_-). So ID size was reduced from 36 to 21 symbols.

## Usage

Install Nano ID using pip:
```
pip install nanoid
```

### Normal

The main module uses URL-friendly symbols (A-Za-z0-9_-) and returns an ID with 21 characters (to have a collision probability similar to UUID v4).

```python
from nanoid import generate

generate() # => NDzkGoTCdRcaRyt7GOepg
```

Symbols `-,.()` are not encoded in the URL. If used at the end of a link they could be identified as a punctuation symbol.

If you want to reduce ID length (and increase collisions probability), you can pass the length as an argument.

```python
from nanoid import generate

generate(size=10) # => "IRFa-VaY2b"
```
Don’t forget to check the safety of your ID length in our ID collision probability calculator.

## Custom Alphabet or Length


If you want to change the ID's alphabet or length you can use the low-level generate module.

```python
from nanoid import generate

generate('1234567890abcdef', 10) # => "4f90d13a42"
```

Non-secure API is also available:

```python
from nanoid import non_secure_generate

non_secure_generate('1234567890abcdef', 10)
```


## Tools

* [ID size calculator](https://zelark.github.io/nano-id-cc/) to choice smaller ID size depends on your case.
nanoid-dictionary with popular alphabets to use with nanoid/generate.
* [`nanoid-dictionary`](https://github.com/aidarkhanov/nanoid-dictionary) with popular alphabets to use.

## Other Programming Languages

* [C#](https://github.com/codeyu/nanoid-net)
* [Clojure and ClojureScript](https://github.com/zelark/nano-id)
* [Crystal](https://github.com/mamantoha/nanoid.cr)
* [Dart](https://github.com/pd4d10/nanoid)
* [Go](https://github.com/matoous/go-nanoid)
* [Elixir](https://github.com/railsmechanic/nanoid)
* [Haskell](https://github.com/4e6/nanoid-hs)
* [Java](https://github.com/aventrix/jnanoid)
* [JavaScript](https://github.com/ai/nanoid) – original implementation.
* [Nim](https://github.com/icyphox/nanoid.nim)
* [PHP](https://github.com/hidehalo/nanoid-php)
* [Ruby](https://github.com/radeno/nanoid.rb)
* [Rust](https://github.com/nikolay-govorov/nanoid)
* [Swift](https://github.com/antiflasher/NanoID)


## Changelog
- v2.0.0
    - Replace ~ to - in default alphabet
    - Add non-secure fast generator
    - Reduce default characters from 22 to 21
- v0.3.0
    - Fix array out of bound error.

## Credits

- [ai](https://github.com/ai) - [nanoid](https://github.com/ai/nanoid)
- [aidarkhanov](https://github.com/aidarkhanov)
