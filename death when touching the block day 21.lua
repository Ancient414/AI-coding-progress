local Players = game:GetService('Players')
local part = game.Workspace.TestPart
local debounce = false

part.Anchored = true
part.Size = Vector3.new(2,2,2)
part.Position = Vector3.new(-12,1,-12)

Players.PlayerAdded:Connect(function(player)
	local leaderstats = Instance.new('Folder')
	leaderstats.Parent = player
	leaderstats.Name = 'leaderstats'
	
	local deaths = Instance.new('IntValue')
	deaths.Parent = leaderstats
	deaths.Name = 'Deaths'
	deaths.Value = 0
end)

part.Touched:Connect(function(hit)
	local player = Players:GetPlayerFromCharacter(hit.Parent)
	
	if player and not debounce then
		debounce = true
		
		local humanoid = hit.Parent:FindFirstChildOfClass('Humanoid')
		
		
		if humanoid then
			humanoid.Health -= 100
		end
		
		player.leaderstats.Deaths.Value += 1
		task.wait(1)
		debounce = false
	end
end)
