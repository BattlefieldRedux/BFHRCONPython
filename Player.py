__author__ = 'Scott Davey'

"""
Base for connecting and querying BFH/BFP4F/BF2 servers using RCON.
Copyright (C) 2013  Scott Davey, www.sd149.co.uk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class Player:
    """
    Representing a player, includes other options for admin tools with their own built in permissions.
    _id: int
    name: str
    kit: str
    kills: int
    deaths: int
    suicides: int
    team: int
    level: int
    score: int
    ping: int
    ip: str
    playerid: int
    vip: int
    heroid: int
    mod: bool, false by default
    admin: bool, false by default
    owner: bool, false by default
    """
    def __init__(self, _id, name, kit, kills, deaths, suicides, team, level, score, ping, ip, playerid, vip, heroid, mod=False, admin=False, owner=False):
        self.id = _id
        self.alive = True
        self.name = name
        if kit == "NA_Gunner_kit" or kit == "RA_Gunner_kit":
            self.kit = "Gunner"
        elif kit == "RA_Soldier_kit" or kit == "NA_Soldier_kit":
            self.kit = "Soldier"
        elif kit == "RA_Commando_kit" or kit == "NA_Commando_kit":
            self.kit = "Commando"
        elif kit == "none":
            self.kit = "Dead"
            self.alive = False
        self.kills = kills
        self.deaths = deaths
        self.suicides = suicides
        if team == 1:
            self.team = "National"
        elif team == 2:
            self.team = "Royal"
        self.level = level
        self.score = score
        self.ping = ping
        self.ip = ip
        self.playerid = playerid
        if vip == 1:
            self.vip = True
        else:
            self.vip = False
        self.heroid = heroid
        self.mod = mod
        self.admin = admin
        self.owner = owner

    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def isAlive(self):
        return self.alive
    def getKit(self):
        return self.kit
    def getKills(self):
        return self.kills
    def getDeaths(self):
        return self.deaths
    def getSuicides(self):
        return self.suicides
    def getTeam(self):
        return self.team
    def getLevel(self):
        return self.level
    def getScore(self):
        return self.score
    def getPing(self):
        return self.ping
    def getIp(self):
        return self.ip
    def getPlayerId(self):
        return self.playerid
    def isVip(self):
        return self.vip
    def getHeroId(self):
        return self.heroid
    def getDeathsSuicides(self):
        return self.deaths-self.suicides
    def isMod(self):
        return self.mod
    def isAdmin(self):
        return self.admin
    def isOwner(self):
        return self.owner



