from main import User , db 
from flask import request

def data():
    buildservername = request.args.get('buildservername')
    if buildservername != 'database':
        query = User.query.filter(db.or_(User.buildserver.like(f'%{buildservername}%')))
    else:
        query = User.query

    # search filter
    search = request.args.get('search[value]')
    if search:
        query = query.filter(db.or_(
            User.buildserver.like(f'%{search}%'),
            User.buildid.like(f'%{search}%'),
            User.date.like(f'%{search}%'),
            User.status.like(f'%{search}%')
        ))
    total_filtered = query.count()

    # sorting
    order = []
    i = 0
    while True:
        col_index = request.args.get(f'order[{i}][column]')
        if col_index is None:
            break
        col_buildid = request.args.get(f'columns[{col_index}][data]')
        if col_buildid not in ['buildid', 'date', 'status']:
            col_buildid = 'buildid'
        descending = request.args.get(f'order[{i}][dir]') == 'asc'
        col = getattr(User, col_buildid)
        if descending:
            col = col.desc()
        else:
            col = col.asc()
        order.append(col)
        i += 1
    if order:
        query = query.order_by(*order)



    # pagination
    start = request.args.get('start', type=int)
    length = request.args.get('length', type=int)
    query = query.offset(start).limit(length)

    if buildservername != 'database':
        counter = User.query.filter(db.or_(User.buildserver.like(f'%{buildservername}%'))).count()
    else:
        counter = User.query.count()

    # response
    return {
        'data': [build.to_dict() for build in query],
        'recordsFiltered': total_filtered,
        'recordsTotal': counter,
        'draw': request.args.get('draw', type=int),
    }
