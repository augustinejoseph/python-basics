## Generator
Generators jis a special type of iterator in Python that helps to produce values on the fly, one at a time, without generating the entire sequence in the memory.

* **yield** = used to produce value and return it to the caller.
After that it pauses its execution, saving its state.
* **next()** = to get the next value from the generator. When called, it resumes the generators previously saved state.