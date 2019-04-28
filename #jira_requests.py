from jira.client import JIRA

url = "https://pycontribs.atlassian.net"
options = {'server': url, 'verify':True}
login = "phystechpozitron@yandex.ru"
pwd = "JVOXIfbaDi0A01UI9Bwx55C9"
jira_client = JIRA(options, basic_auth=(login, pwd))

project = "SCRUM"
issues_in_closed_sprints = jira_client.search_issues('project= ' + project + ' AND sprint in closedSprints()')
issues_in_current_sprint = jira_client.search_issues('project= ' + project + ' AND sprint not in closedSprints() AND sprint not in futureSprints()')

print("Closed sprints info: ")
print()
for issue in issues_in_closed_sprints:
    print("Issue name: ", issue.fields.summary)
    print("Issue reporter: ", issue.fields.reporter)
    print("Status: ", issue.fields.status)
    print()

print("Current sprint info: ")
print()
for issue in issues_in_current_sprint:
    print("Issue name: ", issue.fields.summary)
    print("Issue reporter: ", issue.fields.reporter)
    print("Status: ", issue.fields.status)
    print()