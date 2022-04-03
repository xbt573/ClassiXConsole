import a2s
import sys

servers = {
        "ttt": ("46.174.55.192", 27016),
	"murder": ("46.174.55.192", 27015),
	"prophunt": ("46.174.55.192", 27018),
	"minigames": ("46.174.55.192", 27017)
}

def getstat(servertuple, verbose=False):
	info = a2s.info(servertuple)

	print("Players: " + str(info.player_count))
	print("Map: " + info.map_name)

	if (verbose):
		print("\n")

		print("Server name:" + info.server_name)
		print("Gamemode: " + info.game)
		print("Max players: " + str(info.max_players))
		print("Bot count: " + str(info.bot_count))

		if info.platform == "l":
			platform = "Linux"
		elif info.platform == "w":
			platform = "Windows"
		else:
			platform = "macOS"

		print("Plaform: " + platform)
		print("Password: " + str(info.password_protected))
		print("VAC enabled: " + str(info.password_protected))
		print("Version: " + info.version)


def main():
	if (sys.argv[1] not in servers):
        	print("Wrong server name")
        	sys.exit(0)

	verbose = False

	if ("-v" in sys.argv):
		verbose = True

	getstat(servers[sys.argv[1]], verbose)

if __name__ == '__main__':
	main()
