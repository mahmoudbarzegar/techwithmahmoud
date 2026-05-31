from abc import ABC, abstractmethod
from typing import Protocol

# ABC - Explicit inheritance
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str : pass

class Dog_1(Animal):  # Must inherit
    def speak(self) -> str: return "Woof"

#******************************#    

# Protocol - Structural matching
class Speaker(Protocol):
    def speak(self) -> str: ...

class Dog:  # No inheritance!
    def speak(self) -> str: return "Woof"

class Person:  # No inheritance!
    def speak(self) -> str: return "Hello"

# Both work with Protocol!