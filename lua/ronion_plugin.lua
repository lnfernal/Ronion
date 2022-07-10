local HttpService = game:GetService("HttpService")
local RunService = game:GetService("RunService")

local ServerStorage = game:GetService("ServerStorage")

local event
RunService.Heartbeat:Connect(function()
	local bindable: BindableFunction = game:FindFirstChild("Request")
	if bindable and bindable ~= event then
		event = bindable
		
		bindable.OnInvoke = function(...)
			return HttpService:RequestAsync(...)	
		end
		
	end
end)