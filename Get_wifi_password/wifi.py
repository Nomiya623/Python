import subprocess

def get_profiles():
    try:
        data = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding="mbcs")
        print("Raw data from netsh wlan show profiles command:")
        print(data)
        data = data.split("\n")
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching profiles: {e}")
        return []

def get_password(profile):
    try:
        results = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"], encoding="mbcs")
        print(f"Raw data from netsh wlan show profile {profile} key=clear command:")
        print(results)
        results = results.split("\n")
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        return results[0] if results else ""
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching password for profile {profile}: {e}")
        return ""

def main():
    profiles = get_profiles()
    if not profiles:
        print("No profiles found or an error occurred.")
        return

    for profile in profiles:
        password = get_password(profile)
        print("{:<30}|  {:<}".format(profile, password))

if __name__ == "__main__":
    main()