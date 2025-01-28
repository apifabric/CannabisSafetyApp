import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 258227582612459398 in succeeded_hashes:  # avoid duplicate inserts
            instance = user1 = User(id=1, name="Alice", email="alice@example.com")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(258227582612459398)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1254005928612686227 in succeeded_hashes:  # avoid duplicate inserts
            instance = user2 = User(id=2, name="Bob", email="bob@example.com")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1254005928612686227)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4611053106831759518 in succeeded_hashes:  # avoid duplicate inserts
            instance = user3 = User(id=3, name="Charlie", email="charlie@example.com")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4611053106831759518)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 881259587258516397 in succeeded_hashes:  # avoid duplicate inserts
            instance = user4 = User(id=4, name="David", email="david@example.com")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(881259587258516397)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3000259120618172287 in succeeded_hashes:  # avoid duplicate inserts
            instance = preference1 = Preference(id=1, user_id=1, source_of_plant="GreenHaven", percentage_of_thc=18.5, preferred_branding="EcoCanna")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3000259120618172287)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3243091787236831643 in succeeded_hashes:  # avoid duplicate inserts
            instance = preference2 = Preference(id=2, user_id=2, source_of_plant="SunGrowers", percentage_of_thc=22.0, preferred_branding="Cannaluxe")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3243091787236831643)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7642996279273616780 in succeeded_hashes:  # avoid duplicate inserts
            instance = preference3 = Preference(id=3, user_id=3, source_of_plant="GreenHaven", percentage_of_thc=20.0, preferred_branding="NaturalHigh")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7642996279273616780)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6447445629484483155 in succeeded_hashes:  # avoid duplicate inserts
            instance = preference4 = Preference(id=4, user_id=4, source_of_plant="FarmFresh", percentage_of_thc=15.0, preferred_branding="PurePlant")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6447445629484483155)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5920764844575309870 in succeeded_hashes:  # avoid duplicate inserts
            instance = allergy1 = Allergy(id=1, name="Nuts")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5920764844575309870)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -919163834408743142 in succeeded_hashes:  # avoid duplicate inserts
            instance = allergy2 = Allergy(id=2, name="Gluten")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-919163834408743142)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3988419655464755907 in succeeded_hashes:  # avoid duplicate inserts
            instance = allergy3 = Allergy(id=3, name="Sulfites")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3988419655464755907)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8028383057248694049 in succeeded_hashes:  # avoid duplicate inserts
            instance = allergy4 = Allergy(id=4, name="Dairy")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8028383057248694049)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6017877672970397315 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_allergy1 = UserAllergy(id=1, user_id=1, allergy_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6017877672970397315)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8100689172293087175 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_allergy2 = UserAllergy(id=2, user_id=2, allergy_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8100689172293087175)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6966499126142938935 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_allergy3 = UserAllergy(id=3, user_id=3, allergy_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6966499126142938935)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5241606358255720359 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_allergy4 = UserAllergy(id=4, user_id=4, allergy_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5241606358255720359)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6913166268046848693 in succeeded_hashes:  # avoid duplicate inserts
            instance = outlet_store1 = OutletStore(id=1, name="Downtown Dispensary", location="New York")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6913166268046848693)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2248906935922692403 in succeeded_hashes:  # avoid duplicate inserts
            instance = outlet_store2 = OutletStore(id=2, name="Green Valley", location="Los Angeles")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2248906935922692403)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 9147550720477828743 in succeeded_hashes:  # avoid duplicate inserts
            instance = outlet_store3 = OutletStore(id=3, name="The Green House", location="Seattle")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(9147550720477828743)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1125097764498934194 in succeeded_hashes:  # avoid duplicate inserts
            instance = outlet_store4 = OutletStore(id=4, name="SunnyFields", location="San Francisco")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1125097764498934194)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6715161952134432211 in succeeded_hashes:  # avoid duplicate inserts
            instance = pricing1 = Pricing(id=1, user_id=1, outlet_store_id=1, price=50.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6715161952134432211)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4822676641288136636 in succeeded_hashes:  # avoid duplicate inserts
            instance = pricing2 = Pricing(id=2, user_id=2, outlet_store_id=2, price=45.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4822676641288136636)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1077561190510241092 in succeeded_hashes:  # avoid duplicate inserts
            instance = pricing3 = Pricing(id=3, user_id=3, outlet_store_id=3, price=60.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1077561190510241092)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2056036134582715552 in succeeded_hashes:  # avoid duplicate inserts
            instance = pricing4 = Pricing(id=4, user_id=4, outlet_store_id=4, price=55.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2056036134582715552)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3659246988889050017 in succeeded_hashes:  # avoid duplicate inserts
            instance = branding1 = Branding(id=1, name="EcoCanna")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3659246988889050017)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5483605844397610064 in succeeded_hashes:  # avoid duplicate inserts
            instance = branding2 = Branding(id=2, name="Cannaluxe")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5483605844397610064)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3998139243391647542 in succeeded_hashes:  # avoid duplicate inserts
            instance = branding3 = Branding(id=3, name="NaturalHigh")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3998139243391647542)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2246727834710666221 in succeeded_hashes:  # avoid duplicate inserts
            instance = branding4 = Branding(id=4, name="PurePlant")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2246727834710666221)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6883285603353937197 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_branding1 = UserBranding(id=1, user_id=1, branding_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6883285603353937197)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3606948312518677603 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_branding2 = UserBranding(id=2, user_id=2, branding_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3606948312518677603)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2147074647234266503 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_branding3 = UserBranding(id=3, user_id=3, branding_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2147074647234266503)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5353688647218225974 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_branding4 = UserBranding(id=4, user_id=4, branding_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5353688647218225974)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3076992942581430954 in succeeded_hashes:  # avoid duplicate inserts
            instance = source_of_plant1 = SourceOfPlant(id=1, name="GreenHaven")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3076992942581430954)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5915504148794610684 in succeeded_hashes:  # avoid duplicate inserts
            instance = source_of_plant2 = SourceOfPlant(id=2, name="SunGrowers")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5915504148794610684)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5978077346793288261 in succeeded_hashes:  # avoid duplicate inserts
            instance = source_of_plant3 = SourceOfPlant(id=3, name="FarmFresh")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5978077346793288261)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4392483638834032369 in succeeded_hashes:  # avoid duplicate inserts
            instance = source_of_plant4 = SourceOfPlant(id=4, name="UrbanFarm")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4392483638834032369)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1112861067480956039 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_source_of_plant1 = UserSourceOfPlant(id=1, user_id=1, source_of_plant_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1112861067480956039)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2937658361061745102 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_source_of_plant2 = UserSourceOfPlant(id=2, user_id=2, source_of_plant_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2937658361061745102)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2059604966925834422 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_source_of_plant3 = UserSourceOfPlant(id=3, user_id=3, source_of_plant_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2059604966925834422)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5493607702725225367 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_source_of_plant4 = UserSourceOfPlant(id=4, user_id=4, source_of_plant_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5493607702725225367)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8266154552296450361 in succeeded_hashes:  # avoid duplicate inserts
            instance = thc_percentage1 = ThcPercentage(id=1, value=18.5)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8266154552296450361)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7613538869490759955 in succeeded_hashes:  # avoid duplicate inserts
            instance = thc_percentage2 = ThcPercentage(id=2, value=22.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7613538869490759955)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1380568127578721340 in succeeded_hashes:  # avoid duplicate inserts
            instance = thc_percentage3 = ThcPercentage(id=3, value=15.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1380568127578721340)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2519239888016910588 in succeeded_hashes:  # avoid duplicate inserts
            instance = thc_percentage4 = ThcPercentage(id=4, value=10.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2519239888016910588)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5527284327134007807 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_thc_percentage1 = UserThcPercentage(id=1, user_id=1, thc_percentage_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5527284327134007807)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5118381239600817145 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_thc_percentage2 = UserThcPercentage(id=2, user_id=2, thc_percentage_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5118381239600817145)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8505458500025245559 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_thc_percentage3 = UserThcPercentage(id=3, user_id=3, thc_percentage_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8505458500025245559)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4143408772182289152 in succeeded_hashes:  # avoid duplicate inserts
            instance = user_thc_percentage4 = UserThcPercentage(id=4, user_id=4, thc_percentage_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4143408772182289152)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
