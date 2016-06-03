"""empty message

Revision ID: d9ce546dbcac
Revises: 9ffa798c4399
Create Date: 2016-06-03 09:38:12.089267

"""

# revision identifiers, used by Alembic.
revision = 'd9ce546dbcac'
down_revision = '9ffa798c4399'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('scan_id', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('rule_id', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('file', sa.String(length=512), nullable=True),
    sa.Column('line', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('code', sa.String(length=512), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('task_type', sa.SmallInteger(), nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('branch', sa.String(length=64), nullable=True),
    sa.Column('scan_way', sa.SmallInteger(), nullable=False),
    sa.Column('old_version', sa.String(length=40), nullable=True),
    sa.Column('new_version', sa.String(length=40), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('updated_at', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cobra_task_info')
    op.add_column(u'languages', sa.Column('extensions', sa.String(length=128), nullable=True))
    op.drop_column(u'languages', 'suffix')
    op.add_column(u'projects', sa.Column('author', sa.String(length=50), nullable=True))
    op.add_column(u'projects', sa.Column('last_scan', sa.DateTime(), nullable=True))
    op.add_column(u'projects', sa.Column('remark', sa.String(length=50), nullable=True))
    op.drop_column(u'projects', 'username')
    op.drop_column(u'projects', 'repo_type')
    op.drop_column(u'projects', 'password')
    op.drop_column(u'projects', 'scan_at')
    op.drop_column(u'projects', 'branch')
    op.add_column(u'whitelist', sa.Column('path', sa.String(length=512), nullable=True))
    op.add_column(u'whitelist', sa.Column('status', mysql.TINYINT(), nullable=True))
    op.drop_column(u'whitelist', 'file')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'whitelist', sa.Column('file', mysql.VARCHAR(length=512), nullable=True))
    op.drop_column(u'whitelist', 'status')
    op.drop_column(u'whitelist', 'path')
    op.add_column(u'projects', sa.Column('branch', mysql.VARCHAR(length=128), nullable=True))
    op.add_column(u'projects', sa.Column('scan_at', mysql.DATETIME(), nullable=True))
    op.add_column(u'projects', sa.Column('password', mysql.VARCHAR(length=128), nullable=True))
    op.add_column(u'projects', sa.Column('repo_type', mysql.TINYINT(display_width=2), autoincrement=False, nullable=False))
    op.add_column(u'projects', sa.Column('username', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column(u'projects', 'remark')
    op.drop_column(u'projects', 'last_scan')
    op.drop_column(u'projects', 'author')
    op.add_column(u'languages', sa.Column('suffix', mysql.VARCHAR(length=256), nullable=False))
    op.drop_column(u'languages', 'extensions')
    op.create_table('cobra_task_info',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('task_type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('filename', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('level', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('new_version', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('old_version', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('scan_type', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('scan_way', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('branch', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('tasks')
    op.drop_table('results')
    ### end Alembic commands ###