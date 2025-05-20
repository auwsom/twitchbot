#!/usr
# Twitch API

import twitch

helix = twitch.Helix('$(cat ~/.env/twitch-client-id)', '$(cat ~/.env/twitch-client-secret)')

print(helix.user('mossy_machines').display_name)
