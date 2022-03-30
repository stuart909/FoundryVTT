import roll as r


class Army:
    def __init__(self):
        self.army = self.create_army()


    def create_army(self,leader=None,l_skill=None,support=None,terrain=None,size=None,mercs=None):
        try:
            self.leader = input("Enter General name: ") if leader is None else leader
            self.l_skill = int(input("Enter leader tactical skill")) if l_skill is None else l_skill
            self.support = int(input("Enter support number 0-3: ")) if support is None else support
            self.terrain = int(input("Enter terrain bonus 0-3: ")) if terrain is None else terrain
            self.size = int(input("Enter Army size: ")) if size is None else size
            self.mercs = float(input("Percentage of mercenaries ex: .08: ")) if mercs is None else mercs
            self.soldier_p = 1 - self.mercs - .001 - .01 - .1
        except:
            self.create_army()
        return {"size": self.size, "leader": self.leader, "Tactics": self.l_skill, "support": self.support, "terrain": self.terrain,
                'noble': {'cut': 0, 'pool': 0, 'bodies': self.size * .001 > 1 and self.size * .001 or 1, 'take': .13},
                'special': {'cut': 0, 'pool': 0, 'bodies': self.size * .01 > 1 and self.size * .01 or 1, 'take': 0},
                'obligations': {'cut': 0, 'pool': 0, 'bodies': 1, 'take': .50},
                'soldiers': {'cut': 0, 'pool': 0, 'bodies': self.soldier_p, 'take': .10},
                'mercs': {'cut': 0, 'pool': 0, 'bodies': self.mercs, 'take': 5},
                'support': {'cut': 0, 'pool': 0, 'bodies': self.size * .1 > 1 and self.size * .1 or 1, 'take': 2},
                'bonus': {'cut': 0, 'pool': 0, 'bodies': 1, 'take': 2}}


    def __call__(self):
        return self.army

class Battle:
    def __init__(self, p, e):
        self.p = p
        self.e = e
        self.p_organize = int(input("player army organization number, 0-5:"))
        self.p.update({"tokens":10}) if p["size"] > e["size"] else self.e.update({"tokens":10})
        self.p.update({"tokens":int(10*(p["size"]/e["size"]))}) if "tokens" in e.keys() else self.e.update({"tokens":int(10*(e["size"]/p["size"]))})
        self.p.update({"morale":(p["tokens"]-e["tokens"])}) if e["tokens"] > p["tokens"] else self.e.updateTom({"morale":(e["tokens"]-p["tokens"])})
        self.battleloop()

    def plan(x):
        return r(int(x["Tactics"]/2),1,1,4,False).rolled

    def battleloop(self):
        #battle loop
        while self.p["tokens"] > 0 and self.e["tokens"] > 0:
            try:
                p_plan = int(input("Player Army option | Enter player plan number: "))
            except:
                p_plan = self.plan(self.p)
            e_plan = self.plan(self.e)
            gm_input = 0
            if (p_plan - e_plan) > 4:
                try:
                    gm_input = int(input("Player tactical super advantage strike.  Enter result number: "))
                except:
                    try:
                        gm_input = int(input("Enter the number for player result in battle"))
                    except:
                        gm_input = 0
                p_plan += gm_input
            elif (p_plan - e_plan) < -4:
                try:
                    gm_input = int(input("Player OMG super defense.  Enter result number: "))
                except:
                    try:
                        gm_input = int(input("Enter the number for player result in battle"))
                    except:
                        gm_input = 0
                p_plan += gm_input
            else:
                try:
                    play_num = int(input("enter player amount: "))
                except:
                    play_num = 1
                try:
                    play_stats = [int(input("enter player auto combat result: "))]
                except:
                    play_stats = [0]
                play_damage = []
                for i in play_stats:
                    if i < 4:
                        play_damage.append(r(6,2))

            p_mod = gm_input + p_plan + self.p["support"] + self.p["morale"] + r(self.p["Tactics"],1,1,4,False) + self.p["terrain"]
            e_mod = e_plan + self.e["support"] + self.e["morale"] + r(self.e["Tactics"],1,1,4,False) + self.e["terrain"]
            diff = p_mod - e_mod
            if self.p["tokens"] > self.e["tokens"]:
                self.e["tokens"] -= diff if diff > 0 else diff * -1
            if self.p["tokens"] < self.e["tokens"]:
                self.p["tokens"] -= diff if diff > 0 else diff * -1

    def __call__(self):
        return (self.p,self.e)

def reward(a,m):
    for i in a:
        a[i]["pool"] = (a[i]["take"] / 100) * m
        a[i]["cut"] = a[i]["pool"] / a[i]["bodies"]

a = Army()()
b = Army()()

a,b=Battle(a,b)()