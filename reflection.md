1. How many tests did you write in Part A, and how many lines of production code? What is the ratio? 
Ans: 8 test and around 100 line of code that i write and read and for the ratio is 1 test for every 12.5 line of code
2. When was your bar red for the longest time, and what made it last so long?
Ans: the A7 test_mix addtion because it hard to find the right fomular of the reduce that what reduce is wrong
3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right? 
Ans: 1.Where used: In Step A6, returning a hardcoded grams(500) inside plus and having Converter. 2. In Step A2, adding a second multiplication test (test_multiplication_by_two) 3.In Step A8 (or Sum.plus), implementing def plus(self, other): return Sum(self, other) directly. and each choise was right.
4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
Ans: Looking at my notes, I still have subtraction, division, and handling missing conversion rates on my list. I also jotted down making Quantity hashable back in Step A4.   I would probably implement subtraction next since it naturally fits with addition for adjusting recipes.I would cross off the __hash__ method. I only added it to the list because the lab pointed out that adding __eq__ makes the object unhashable. But since I don't actually need to use Quantity objects as dictionary keys or put them in sets right now, building it would just be guessing at future requirements.
5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
Ans: probably not. If I had planned the architecture on paper, I likely would have just written an if/else block inside Converter.reduce to check if it was looking at a Quantity or a Sum.
6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design? 
Ans: in my oppinion i like the part 0 before part A because this can handle the code while the code is finish and can build the full test =.