def create_contract(self, parent1_name, parent1_email, parent1_phone, parent1_cert,
                    parent2_name=None, parent2_email=None, parent2_phone=None, parent2_cert=None,
                    kin_name=None, kin_phone=None,
                    child_name=None, child_gender=None, child_age=None, ai_friend_name=None, disabilities=None):
    
    contract = {
        "parents": [{
            "name": parent1_name, "email": parent1_email, "phone": parent1_phone,
            "birth_cert": self.cipher.encrypt(open(parent1_cert, 'rb').read()).decode()
        }],
        "next_of_kin": {}
    }
    
    if parent2_name:
        contract["parents"].append({
            "name": parent2_name, "email": parent2_email, "phone": parent2_phone,
            "birth_cert": self.cipher.encrypt(open(parent2_cert, 'rb').read()).decode()
        })
    
    if kin_name:
        contract["next_of_kin"] = {"name": kin_name, "phone": kin_phone}
    
    contract.update({
        "child": {"name": child_name, "gender": child_gender, "age": child_age, "disabilities": disabilities or []},
        "ai": {"friend_name": ai_friend_name},
        "geo_enabled": True,
        "voice_proxy_in_crisis": True
    })
    
    self.save_contract(contract)
    return "Contract sealed. Eden is ready — for every family."
