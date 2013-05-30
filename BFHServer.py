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

from ServerBase import ServerBase
from Player import Player

class BFHServer(ServerBase):
    """
    Adds methods for interacting with a BFH server
    """

    def getPlayers(self):
        """
        Returns players current in-game.
        returns: tuple of Player objects
        """
        result = self.query("bf2cc pl", True)
        result = result.split("\\r")
        playersList = []
        for each in result:
            playerList = each.split("\\t")
            playersList.append(playerList)
        playersList.pop(-1) #Ended with \\t, so creates empty item, removing it
        currentPlayers = []
        for each in playersList:
            currentPlayers.append(Player(each[0], each[1], each[34], each[31],
                each[36], each[30], each[2], each[39], each[37], each[3], each[18], each[47], each[46], each[10]))
        return tuple(currentPlayers)

    def getClientChatBuffer(self):
        """
        Get's new chat, only returns chat that hasn't been recieved already. So this can be called again
        and again, no need to check for repeats.
        returns: A tuple of tuples.
        """
        allChat = []
        chat = self.query('bf2cc clientchatbuffer')
        chat = chat.split("\\r\\r")
        chat.pop(-1) #empty element created at end of list, remove it
        for each in chat:
            chatList = tuple(each.split("\\t"))
            allChat.append(chatList)
        return tuple(allChat)

    def getServerInfo(self):
        """
        Returns information about the server
        returns: tuple
        """
        info = self.query('bf2cc si', True).replace("\\n", "")
        return tuple(info.split("\\t"))

    def warnPlayer(self, player, msg):
        """
        Warning a player, does not use the proper warning method as it does not
        show correctly in-game. Making use of admin say instead.
        player: str (must be full name, this method will not auto-complete it for you)
        msg: str
        returns: str
        """
        return self.query('exec game.sayAll "WARN: {0} REASON: {1}"'.format(player, msg))

    def kickPlayer(self, player, reason):
        """
        Kicks a player from server.
        player: str
        reason: str
        returns: str
        """
        return self.query('kick {0} "{1}"'.format(player, reason))
