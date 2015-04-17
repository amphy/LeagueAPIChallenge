#!/usr/bin/env python
import os
import sys

from flask import Flask, render_template
app = Flask(__name__)

import views
