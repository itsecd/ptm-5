import pytest
import torch
from unittest.mock import patch
from commons import kl_divergence, rand_slice_segments, get_padding, intersperse, sequence_mask, add_timing_signal_1d, cat_timing_signal_1d  

@pytest.mark.parametrize("m_p, logs_p, m_q, logs_q", [
    (torch.tensor([1.0]), torch.tensor([1.0]), torch.tensor([1.0]), torch.tensor([1.0])),
    (torch.tensor([0.0]), torch.tensor([0.0]), torch.tensor([0.0]), torch.tensor([0.0])),
])
def test_kl_divergence(m_p, logs_p, m_q, logs_q):
    result = kl_divergence(m_p, logs_p, m_q, logs_q)
    assert isinstance(result, torch.Tensor)

@pytest.mark.parametrize("input_shape, segment_size, expected_shape", [
    ((1, 2, 10), 4, ((1, 2, 4), (1,))),
])
def test_rand_slice_segments(input_shape, segment_size, expected_shape):
    x = torch.rand(input_shape)

    with patch('torch.rand') as mock_rand:
        mock_rand.return_value = torch.tensor([0.5])
        result, ids_str = rand_slice_segments(x, segment_size=segment_size)

    assert result.shape == expected_shape[0]
    assert ids_str.shape == expected_shape[1]

@pytest.mark.parametrize("kernel_size, dilation, expected", [
    (3, 1, 1),
    (5, 1, 2),
])
def test_get_padding(kernel_size, dilation, expected):
    assert get_padding(kernel_size, dilation) == expected

def test_cat_timing_signal_1d():
    batch_size, channels, length = 1, 10, 50
    x = torch.randn(batch_size, channels, length)

    result = cat_timing_signal_1d(x, axis=1)
    
    expected_channels = channels * 2
    assert result.shape == (batch_size, expected_channels, length)

    assert torch.equal(result[:, :channels, :], x) 
    assert not torch.equal(result[:, channels:, :], x) 


def test_add_timing_signal_1d():
    batch_size, channels, length = 2, 10, 50
    x = torch.randn(batch_size, channels, length)

    result = add_timing_signal_1d(x)

    assert result.shape == x.shape

    assert not torch.equal(result, x)

def test_intersperse():
    lst = [1, 2, 3]
    item = 0
    result = intersperse(lst, item)
    assert result == [0, 1, 0, 2, 0, 3, 0]

def test_sequence_mask():
    length = torch.tensor([3, 4, 5])
    max_length = 6
    mask = sequence_mask(length, max_length)
    expected_mask = torch.tensor([
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0]
    ])
    assert torch.equal(mask, expected_mask)
