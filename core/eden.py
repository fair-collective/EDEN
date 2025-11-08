def respond(self, child_input):
    if "lost" in child_input:
        return self.geo.send_pin(self.child_name) + " I'm guiding you home."
    
    if "scared" in child_input and self.age < 10:
        return "You're brave. Want to try telling your teacher? I’ll help you practice."
    
    if "do it" in child_input:
        return "You can! Try first. I’ll cheer when you win."
    
    return f"You're growing strong, {self.child_name}."
