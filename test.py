from cgi import test
from pyclbr import Class
import unittest
import cracker

class Test_hackman(unittest.TestCase):
    
    
    def test_for_incorrect_input_from_user(self):
        
        demo_invalid_input = "T"
        demo_get_input = cracker.validate_user_input(demo_invalid_input)
        self.assertFalse(demo_get_input)
        
        
    def test_for_correct_input_from_user(self):
    
        demo_correct_input = "1"
        demo_get_input = cracker.validate_user_input(demo_correct_input)
        self.assertTrue(demo_get_input)
                
        
    def test_valid_guess(self):
        
        guess = "12345"
        actual_code = "12345"
        check_guess_is_equal_to_pin = cracker.correct_guess(guess, actual_code)
        self.assertTrue(check_guess_is_equal_to_pin)


    def test_invalid_guess(self):
        
        guess = "12345"
        actual_code = "1234"
        check_guess_is_equal_to_pin = cracker.correct_guess(guess, actual_code)
        self.assertFalse(check_guess_is_equal_to_pin)
        
        
    def test_game_intro(self):
        
        self.assertEquals("Choose game level\n"+
      "-easy\n"+
      "-normal\n"+
      "-hard\n", cracker.game_mode_prompt())
        
        
if __name__ == '__main__':
    unittest.main()