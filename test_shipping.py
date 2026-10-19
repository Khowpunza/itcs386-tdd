from shipping import shipping_fee
import pytest


# Test rule 1 that weigth > 0 it need to fail when add the number > 0 but in this case add 0 will turn fail it not correct
# that 0 need to test pass
@pytest.mark.parametrize("weight" , 
 [
-0.1,
-0.5,
-1,
0
                         ])
def test_rule_1(weight):
    with pytest.raises(ValueError , match="weight must be more than 0 kg"):
        shipping_fee(weight) 

# Test rule 2 that weigth <= 1 it need to return 40 baht but in this case when add 1 it fail it not correct that 1 need to test pass
@pytest.mark.parametrize("weight, expected" ,
[
(1,40),
(0.1,40),
(0.5,40)
                             
                         ])
def test_rule_2(weight, expected):
    assert shipping_fee(weight) == expected


# Test rule 3 that weigth > 1 and <= 5 it need to return 60 baht this test is pass because the weight is in the range of 1 and 5
@pytest.mark.parametrize("weight, expected", [
    (1.1, 60),
    (3.5, 60),
    (5.0, 60),
])
def test_rule_3_up_to_5_kg(weight, expected):
    assert shipping_fee(weight) == expected


# Test rule 4 that weight > 5 but it test fail because 5.1 and 5.2 is in the range of weight > 5 but 
# it return 70 baht but the test is fail because the expected is 60 baht when 5.1-5 = 0.1 but in int
# it will return 0 so the expected is 60 baht but the test is fail because the expected is 70 baht 
@pytest.mark.parametrize("weight, expected", [
    (5.1, 70),
    (5.2, 70),
    (6.0, 70),
    (6.1, 80),
    (10.0, 110),
])
def test_rule_4_above_5_kg(weight, expected):
    assert shipping_fee(weight) == expected