def route(task: str) -> str:
    t = task.lower()
    if "security" in t:
        return "security_prompt_sentinel"
    if "revenue" in t:
        return "ho_revenue_exploit_lab"
    return "system_pro_integrator"
