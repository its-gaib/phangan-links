"""Summarize recorded link checks without implying a directory-wide recheck."""
from datetime import date
import re


def verification_summary(entries):
    recorded = []
    for entry in entries:
        value = entry.get('checkedAt')
        if value is None or value == '':
            continue
        try:
            if not isinstance(value, str) or not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', value):
                raise ValueError()
            parsed = date.fromisoformat(value)
        except ValueError:
            raise ValueError(f"Invalid checkedAt date for entry: {entry['id']}") from None
        recorded.append(parsed.isoformat())
    return {
        'totalCount': len(entries),
        'checkedCount': len(recorded),
        'missingCheckCount': len(entries) - len(recorded),
        'earliestCheckedAt': min(recorded) if recorded else None,
        'latestCheckedAt': max(recorded) if recorded else None,
    }


def shared_check_date(summary):
    """Retain the legacy date only when it accurately describes every entry."""
    if (summary['checkedCount'] and summary['checkedCount'] == summary['totalCount']
            and summary['earliestCheckedAt'] == summary['latestCheckedAt']):
        return summary['latestCheckedAt']
    return None


def verification_text(summary):
    checked = summary['checkedCount']
    total = summary['totalCount']
    missing = summary['missingCheckCount']
    if checked:
        start = summary['earliestCheckedAt']
        end = summary['latestCheckedAt']
        period = start if start == end else f'{start} to {end}'
        text = f'Recorded checks: {checked} of {total} links, dated {period}.'
    else:
        text = f'No check dates are recorded for the {total} links.'
    if missing and checked:
        text += f' {missing} link{"s" if missing != 1 else ""} {"have" if missing != 1 else "has"} no recorded check date.'
    return text
