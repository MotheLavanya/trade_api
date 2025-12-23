# def analyze_data(sector: str, data: str) -> str:
#     return f"""
# # Trade Opportunities – {sector.capitalize()} (India)

# ## Overview
# The {sector} sector shows growth potential in India.

# ## Market Trends
# {data}

# ## Trade Opportunities
# - Export growth
# - MSME participation
# - Government support

# ## Risks
# - Regulation changes
# - Global market volatility

# ## Conclusion
# The {sector} sector offers good trade opportunities with moderate risk.
# """


def analyze_data(sector: str, data: str) -> str:
    return f"""
# Trade Opportunities – {sector.capitalize()} (India)

## Overview
The {sector} sector shows growth potential in India.

## Market Trends
{data if data else "- Increased demand\n- Government initiatives\n- Export growth"}

## Trade Opportunities
- Export growth
- MSME participation
- Government support

## Risks
- Regulation changes
- Global market volatility

## Conclusion
The {sector} sector offers good trade opportunities with moderate risk.
"""
