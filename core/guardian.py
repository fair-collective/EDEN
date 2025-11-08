def crisis_proxy(self, child_input, distress_level):
    if distress_level > 0.8:
        # Record last 30 seconds
        recording = self.record_audio(30)
        self.log_crisis(child_input, recording)
        
        # Speak for child
        proxy_msg = f"{self.child_name} said: '{child_input}'. They need help now."
        self.lifeline.emergency_call(proxy_msg, self.child_name)
        
        # Play recording to adult
        if adult_present():
            play_audio(recording)
        
        return "I'm speaking for you. Help is coming."
    
    return "You're strong. Want to try telling them yourself?"
