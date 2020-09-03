from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import fintech.QTS_SMA as SMA
import json


@require_http_methods(["POST"])
def getFitness(request):
    ma_stockPrice = [51.708538, 51.486591, 52.53714, 51.400280, 50.312748, 47.678982, 48.581562, 49.084641, 50.167248,
                     49.753849, 49.627602, 51.729252, 50.189526, 49.939507, 51.117813, 52.070862, 52.073338, 52.637737,
                     52.593182, 50.162300, 51.115337, 50.538563, 50.877701, 51.739151, 51.672314, 50.919777, 51.783714,
                     52.796162, 52.791210, 53.016479, 53.642761, 55.348343, 55.224567, 54.150230, 54.434902, 54.632942,
                     55.145359, 54.697304, 53.897728, 54.142803, 53.885353, 54.714626, 54.432430, 54.167561, 55.442406,
                     55.595886, 54.202213, 54.662643, 56.194942, 56.207317, 55.548851, 56.199894, 56.957375, 58.472343,
                     58.388180, 58.252033, 58.016861, 58.242130, 58.521858, 59.536781, 59.400635, 60.197727, 60.296741,
                     61.039375, 61.650810, 60.224953, 60.217525, 61.579021, 63.326683, 63.742554, 63.650970, 63.678192,
                     64.413116, 64.589409, 65.100876, 65.041283, 65.664490, 65.210121, 65.984779, 66.317490, 66.116371,
                     65.346687, 65.053703, 64.996597, 66.136230, 65.619789, 66.501213, 66.354729, 65.587517, 64.418091,
                     64.986664, 65.940086, 67.213799, 66.272789, 66.660126, 67.228699, 67.400017, 68.316193, 69.485619,
                     69.622192, 69.455833, 69.525352, 69.381348, 70.513535, 70.580566, 71.980911, 71.953598, 72.380653,
                     72.909500, 74.573036, 73.848030, 74.436470, 74.086395, 75.278160, 76.877136, 77.050926, 78.697075,
                     77.634407, 77.301704, 78.270020, 79.136551, 78.600250, 78.880821, 79.260696, 79.032265, 76.708298,
                     78.878326, 80.529434, 80.412743, 76.847343, 76.636299, 79.166336, 79.811897, 80.745445, 79.647896,
                     80.026192, 79.543365, 81.432350, 80.852463, 80.872375, 79.391556, 80.541367, 79.715088, 77.910744,
                     74.209946, 71.696297, 72.833664, 68.072662, 68.032837, 74.366737, 72.004913, 75.344826, 72.900864,
                     71.932739, 66.243423, 71.014381, 68.548012, 61.778580, 69.180161, 60.280346, 62.930878, 61.390331,
                     60.919952, 57.052418, 55.840385, 61.442596, 61.104122, 64.319611, 61.656628, 63.416183, 63.286770,
                     59.956806, 60.957287, 60.081242, 65.322578, 64.565994, 66.218536, 66.696373, 68.005470, 71.439957,
                     70.787903, 71.350365, 70.382233, 68.921326, 66.790947, 68.714760, 68.448463, 70.424545, 70.474319,
                     69.331970, 71.609200, 73.119873, 71.942688, 72.960594, 74.055649, 74.819695, 75.593697, 77.392960,
                     78.610764, 77.712387, 76.774071, 77.245728, 76.789047, 78.598282, 78.144112, 79.663872, 79.069939,
                     79.579025, 79.039993, 79.384369, 79.419304, 79.341949, 80.317688, 80.689514, 81.133713, 80.434975,
                     82.725845, 83.214958, 85.842720, 88.051239, 83.823860, 84.547554, 85.593170, 87.861580, 87.739304,
                     87.774246, 87.272644, 89.556030, 91.467583, 89.852997, 91.045845, 88.248390, 90.282219, 91.035858,
                     90.863670, 90.863670, 93.294289, 93.004814, 95.170906, 95.580170, 95.747368, 95.305664, 96.882820,
                     97.549118, 96.348778, 96.154129, 98.180481, 96.825424, 97.097435, 92.677902, 92.448311, 94.639359,
                     93.084671, 94.868950, 96.016884, 106.068756, 108.741440, 109.467628, 109.864410, 113.697502,
                     111.112503, 112.727501, 109.375000, 113.010002, 115.010002, 114.907501, 114.607498, 115.562500,
                     115.707497, 118.275002, 124.370003, 125.857498, 124.824997, 126.522499, 125.010002, 124.807503,
                     129.04]
    # TODO: 從資料庫抓股價

    return JsonResponse(SMA.QTS(ma_stockPrice))


@require_http_methods(["POST"])
def custom(request):
    ma_stockPrice = [51.708538, 51.486591, 52.53714, 51.400280, 50.312748, 47.678982, 48.581562, 49.084641, 50.167248,
                     49.753849, 49.627602, 51.729252, 50.189526, 49.939507, 51.117813, 52.070862, 52.073338, 52.637737,
                     52.593182, 50.162300, 51.115337, 50.538563, 50.877701, 51.739151, 51.672314, 50.919777, 51.783714,
                     52.796162, 52.791210, 53.016479, 53.642761, 55.348343, 55.224567, 54.150230, 54.434902, 54.632942,
                     55.145359, 54.697304, 53.897728, 54.142803, 53.885353, 54.714626, 54.432430, 54.167561, 55.442406,
                     55.595886, 54.202213, 54.662643, 56.194942, 56.207317, 55.548851, 56.199894, 56.957375, 58.472343,
                     58.388180, 58.252033, 58.016861, 58.242130, 58.521858, 59.536781, 59.400635, 60.197727, 60.296741,
                     61.039375, 61.650810, 60.224953, 60.217525, 61.579021, 63.326683, 63.742554, 63.650970, 63.678192,
                     64.413116, 64.589409, 65.100876, 65.041283, 65.664490, 65.210121, 65.984779, 66.317490, 66.116371,
                     65.346687, 65.053703, 64.996597, 66.136230, 65.619789, 66.501213, 66.354729, 65.587517, 64.418091,
                     64.986664, 65.940086, 67.213799, 66.272789, 66.660126, 67.228699, 67.400017, 68.316193, 69.485619,
                     69.622192, 69.455833, 69.525352, 69.381348, 70.513535, 70.580566, 71.980911, 71.953598, 72.380653,
                     72.909500, 74.573036, 73.848030, 74.436470, 74.086395, 75.278160, 76.877136, 77.050926, 78.697075,
                     77.634407, 77.301704, 78.270020, 79.136551, 78.600250, 78.880821, 79.260696, 79.032265, 76.708298,
                     78.878326, 80.529434, 80.412743, 76.847343, 76.636299, 79.166336, 79.811897, 80.745445, 79.647896,
                     80.026192, 79.543365, 81.432350, 80.852463, 80.872375, 79.391556, 80.541367, 79.715088, 77.910744,
                     74.209946, 71.696297, 72.833664, 68.072662, 68.032837, 74.366737, 72.004913, 75.344826, 72.900864,
                     71.932739, 66.243423, 71.014381, 68.548012, 61.778580, 69.180161, 60.280346, 62.930878, 61.390331,
                     60.919952, 57.052418, 55.840385, 61.442596, 61.104122, 64.319611, 61.656628, 63.416183, 63.286770,
                     59.956806, 60.957287, 60.081242, 65.322578, 64.565994, 66.218536, 66.696373, 68.005470, 71.439957,
                     70.787903, 71.350365, 70.382233, 68.921326, 66.790947, 68.714760, 68.448463, 70.424545, 70.474319,
                     69.331970, 71.609200, 73.119873, 71.942688, 72.960594, 74.055649, 74.819695, 75.593697, 77.392960,
                     78.610764, 77.712387, 76.774071, 77.245728, 76.789047, 78.598282, 78.144112, 79.663872, 79.069939,
                     79.579025, 79.039993, 79.384369, 79.419304, 79.341949, 80.317688, 80.689514, 81.133713, 80.434975,
                     82.725845, 83.214958, 85.842720, 88.051239, 83.823860, 84.547554, 85.593170, 87.861580, 87.739304,
                     87.774246, 87.272644, 89.556030, 91.467583, 89.852997, 91.045845, 88.248390, 90.282219, 91.035858,
                     90.863670, 90.863670, 93.294289, 93.004814, 95.170906, 95.580170, 95.747368, 95.305664, 96.882820,
                     97.549118, 96.348778, 96.154129, 98.180481, 96.825424, 97.097435, 92.677902, 92.448311, 94.639359,
                     93.084671, 94.868950, 96.016884, 106.068756, 108.741440, 109.467628, 109.864410, 113.697502,
                     111.112503, 112.727501, 109.375000, 113.010002, 115.010002, 114.907501, 114.607498, 115.562500,
                     115.707497, 118.275002, 124.370003, 125.857498, 124.824997, 126.522499, 125.010002, 124.807503,
                     129.04]
    body = json.loads(request.body)
    strategy = {'buy1': body['buy1'], 'buy2': body['buy2'], 'sell1': body['sell1'], 'sell2': body['sell2']}
    holding_period, profit = SMA.fitness(ma_stockPrice, [body['buy1'], body['buy2'], body['sell1'], body['sell2']])
    # TODO: 從資料庫抓股價

    context = {'stock price': ma_stockPrice[256:], 'holding period': holding_period, 'profit': profit,
               'strategy': strategy}
    return JsonResponse(context)
